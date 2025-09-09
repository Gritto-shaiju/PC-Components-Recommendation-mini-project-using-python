import pc_functions
import select_budget_split
import sys
from datetime import datetime


# asking for budget and preference from user
print("gaming:1\nproductivity:2\nworkspace:3\ncustom:4")
preference = input("Enter your pc preference from above |1,2,3,4|:")
obj1=pc_functions.Pc()
if preference == "4":
    cpu_budget=int(input("Enter budget for cpu(processor):"))
    gpu_want=input("do you want separate graphics card [yes|no]:")
    if gpu_want == "yes":
        gpu_budget=int(input("Enter budget for graphics card:"))
    else:
        gpu_budget = 0
    motherboard_budget=int(input("Enter budget for motherboard:"))
    ram_budget=int(input("Enter budget for RAM:"))
    storage_budget=int(input("Enter budget for storage:"))
    psu_budget=int(input("Enter budget for power supply:"))
    case_budget=int(input("Enter budget for cabinet:"))
    cooler_want=input("do you want separate CPU cooler [yes|no]:")
    if cooler_want == "yes":
        cooler_budget=int(input("Enter budget for CPU cooler:"))
    else:
        cooler_budget = 0
    split = obj1.custom_split(cpu_budget,gpu_budget,motherboard_budget,ram_budget,storage_budget,psu_budget,case_budget,cooler_budget)
    budget = sum(split.values())
    build = obj1.build_pc(split)

else:
    budget = int(input("Enter your pc budget:"))
    # asking user do want separate cooler if budget greater than 600000 
    if budget != " " and budget>60000:
        cpu_cool = input("do you want separate cpu cooler [yes|no]:")
    else:
        cpu_cool="no"
    # exit program if gaming budget is low
    if preference == "1" and budget<30000:
        print(f"Gaming pc budget is low")
        sys.exit()
    # calling functions to split budget and build pc recomentation
    split = select_budget_split.split_select(preference,cpu_cool,budget)
    if split == "invalid preference":
        print("Invalid preference")
        sys.exit()
    else:
        build = obj1.build_pc(split)

# name and checking phone number
name=input("Enter your name:")
phone=input("Enter your phone:")
while (True):
    if phone.isdigit() and len(phone)==10:
        break
    else:
        phone=input("Enter a valid phone number:")

# writing recomentation in file
current_date =datetime.now()
file = open("pc_bill.txt","w")
file.write(f" Your PC BUILD RECOMMENDATION {" ".ljust(30)} Date:{current_date.date()}\n============================= {" ".ljust(30)} Time:{current_date.time().replace(microsecond=0)}\nNAME:{name.capitalize()}\nPHONE:{phone}\n\nCOMPONENTS\n")
total=0
for category, item in build.items():
    for component_name, price in item.items():
        category=category.upper()
        file.write(f"{category.ljust(12)} : {component_name.ljust(50)} {str(price).rjust(6)}\n")
        total+=price

file.write(f"\nApprox total : {" ".ljust(50)} {str(total).rjust(6)}\nU can buy periferals for :{budget-total}")

history_file = open("history.txt","a")

history_file.write(f"\n\nDate:{current_date.date()}\nTime:{current_date.time().replace(microsecond=0)}\n\nName:{name}\nPhone:{phone}\nPreference:{preference}\nBudget:{budget}\n\n===============================================\n")

print("PC BUILD RECOMENTATION IS IN FILE pc_bill.py")


