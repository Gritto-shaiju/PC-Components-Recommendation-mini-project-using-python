import numpy as np
import pandas as pd


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
        df = pd.read_csv('pc_components.csv',sep=',')
        for component, budget in split.items():
            if component == "cpu_budget":
                filtered_df = df[(df['Category'] == 'cpu') & (df['Price'] <= budget)]
                build['cpu'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "gpu_budget":
                filtered_df = df[(df['Category'] == 'gpu') & (df['Price'] <= budget)]
                build['gpu'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "motherboard_budget":
                filtered_df = df[(df['Category'] == 'motherboard') & (df['Price'] <= budget)]
                build['motherboard'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "ram_budget":
                filtered_df = df[(df['Category'] == 'ram') & (df['Price'] <= budget)]
                build['ram'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "storage_budget":
                filtered_df = df[(df['Category'] == 'storage') & (df['Price'] <= budget)]
                build['storage'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "psu_budget":
                filtered_df = df[(df['Category'] == 'psu') & (df['Price'] <= budget)]
                build['psu'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "case_budget":
                filtered_df = df[(df['Category'] == 'cases') & (df['Price'] <= budget)]
                build['case'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            elif component == "cooler_budget":
                filtered_df = df[(df['Category'] == 'coolers') & (df['Price'] <= budget)]
                build['cooler'] = filtered_df.loc[filtered_df['Price'].idxmax()][['Component','Price']].to_dict() if not filtered_df.empty else None
            else:
                continue

        return build
