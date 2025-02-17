import pandas as pd


data = pd.read_csv('/home/kev-man/Models/Datasets/archive (2)/')


data= data.drop(columns=["PhysicalActivityLevel","Gender"])

data_cleaned= data
def clean_row(data):
    data_cleaned = data.dropna()
    return data_cleaned
print(data_cleaned.columns)




