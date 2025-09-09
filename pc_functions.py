
from data import pc_components

class Pc:
         
    def gaming_split(self,budget):
        cpu_budget=round(budget*0.22)
        gpu_budget=round(budget*0.35)
        motherboard_budget=round(budget*0.15)
        ram_budget=round(budget*0.10)
        storage_budget=round(budget*0.08)
        psu_budget=round(budget*0.05)
        case_budget=round(budget*0.05)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget,}
    
    def gaming_split_cooler(self,budget):
        cpu_budget=round(budget*0.22)
        gpu_budget=round(budget*0.30)
        motherboard_budget=round(budget*0.15)
        ram_budget=round(budget*0.10)
        storage_budget=round(budget*0.08)
        psu_budget=round(budget*0.05)
        case_budget=round(budget*0.05)
        cooler_budget=round(budget*0.05)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget, "cooler_budget":cooler_budget}
    
    
    def productivity_split(self,budget):
        cpu_budget=round(budget*0.25)
        gpu_budget=round(budget*0.25)
        motherboard_budget=round(budget*0.15)
        ram_budget=round(budget*0.10)
        storage_budget=round(budget*0.12)
        psu_budget=round(budget*0.08)
        case_budget=round(budget*0.05)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget,}

    def productivity_split_cooler(self,budget):
        cpu_budget=round(budget*0.25)
        gpu_budget=round(budget*0.25)
        motherboard_budget=round(budget*0.12)
        ram_budget=round(budget*0.10)
        storage_budget=round(budget*0.10)
        psu_budget=round(budget*0.08)
        case_budget=round(budget*0.05)
        cooler_budget=round(budget*0.05)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget, "cooler_budget":cooler_budget}
    

    def workspace_split(self,budget):
        cpu_budget=round(budget*0.35)
        gpu_budget=round(budget*0.05)
        motherboard_budget=round(budget*0.14)
        ram_budget=round(budget*0.16)
        storage_budget=round(budget*0.18)
        psu_budget=round(budget*0.08)
        case_budget=round(budget*0.04)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget,}
    
    def workspace_split_cooler(self,budget):
        cpu_budget=round(budget*0.35)
        gpu_budget=round(budget*0.05)
        motherboard_budget=round(budget*0.12)
        ram_budget=round(budget*0.16)
        storage_budget=round(budget*0.18)
        psu_budget=round(budget*0.06)
        case_budget=round(budget*0.04)
        cooler_budget=round(budget*0.04)
        return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget, "cooler_budget":cooler_budget}

    def custom_split(self,cpu_budget,gpu_budget,motherboard_budget,ram_budget,storage_budget,psu_budget,case_budget,cooler_budget):
                return {"cpu_budget":cpu_budget, "gpu_budget":gpu_budget, "motherboard_budget":motherboard_budget, "ram_budget":ram_budget, "storage_budget":storage_budget, "psu_budget":psu_budget, "case_budget":case_budget, "cooler_budget":cooler_budget}


    def build_pc(self,split):
        build={}
        for i in pc_components:
            
            if i == "cpu":
                cart={}
                for j in pc_components["cpu"]:
                    if pc_components["cpu"][j]<=split["cpu_budget"]:        
                        cart[j]=pc_components["cpu"][j]
                if cart == {}:
                    cart["none"]=0
                    build["cpu"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["cpu"]={max_key:cart[max_key]}
        
            elif i == "gpu":
                cart={}
                for j in pc_components["gpu"]:
                    if pc_components["gpu"][j]<=split["gpu_budget"]:
                        cart[j]=pc_components["gpu"][j]
                if cart == {}:
                    cart["Integrated CPU Graphics"]=0
                    build["gpu"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["gpu"]={max_key:cart[max_key]}
        
            elif i == "motherboard":
                cart={}
                for j in pc_components["motherboard"]:
                    if pc_components["motherboard"][j]<=split["motherboard_budget"]:
                        cart[j]=pc_components["motherboard"][j]
                if cart == {}:
                    cart["none"]=0
                    build["motherboard"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["motherboard"]={max_key:cart[max_key]}
        
            elif i == "ram":
                cart={}
                for j in pc_components["ram"]:
                    if pc_components["ram"][j]<=split["ram_budget"]:
                        cart[j]=pc_components["ram"][j]
                if cart == {}:
                    cart["none"]=0
                    build["ram"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["ram"]={max_key:cart[max_key]}
        
            elif i == "storage":
                cart={}
                for j in pc_components["storage"]:
                    if pc_components["storage"][j]<=split["storage_budget"]:
                        cart[j]=pc_components["storage"][j]
                if cart == {}:
                    cart["none"]=0
                    build["storage"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["storage"]={max_key:cart[max_key]}
        
            elif i == "psu":
                cart={}
                for j in pc_components["psu"]:
                    if pc_components["psu"][j]<=split["psu_budget"]:
                        cart[j]=pc_components["psu"][j]
                if cart == {}:
                    cart["none"]=0
                    build["psu"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["psu"]={max_key:cart[max_key]}
        
            elif i == "cases":
                cart={}
                for j in pc_components["cases"]:
                    if pc_components["cases"][j]<=split["case_budget"]:
                        cart[j]=pc_components["cases"][j]
                if cart == {}:
                    cart["none"]=0
                    build["cases"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["cases"]={max_key:cart[max_key]}
        
            elif i == "coolers":
                cart={}
                for j in pc_components["coolers"]:
                    if "cooler_budget" in split.keys():
                        if pc_components["coolers"][j]<=split["cooler_budget"]:
                            cart[j]=pc_components["coolers"][j]
                if cart == {}:
                    cart["stock cooler"]=0
                    build["coolers"]=cart
                else:
                    max_key=max(cart,key=cart.get)
                    build["coolers"]={max_key:cart[max_key]}
    
        return build
