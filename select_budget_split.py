from pc_functions import Pc
obj2 = Pc()

def split_select(preference,cpu_cool,budget):
    
    if preference =="1":
        if cpu_cool.lower()=="yes":
            return obj2.gaming_split_cooler(budget)
            
        else:
            return obj2.gaming_split(budget)
    
    elif preference == "2":
        if cpu_cool.lower() == "yes":
            return obj2.productivity_split_cooler(budget)
    
        else:
            return obj2.productivity_split(budget)
    
    elif preference == "3":
        if cpu_cool.lower() == "yes":
            return obj2.workspace_split_cooler(budget)
        else:
            return obj2.workspace_split(budget)
        
    else:
        return "invalid preference"