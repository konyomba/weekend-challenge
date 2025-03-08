import pandas as pd


data = pd.read_csv('/home/kev-man/Models/Datasets/archive (2)/obesity_data.csv')
data_d=pd.read_csv('/home/kev-man/Models/Datasets/archive (2)/diabetes_data_upload.csv')

data= data.drop(columns=["PhysicalActivityLevel","Gender"])



data_cleaned= data
def clean_row(data):
    data_cleaned = data.dropna()
    return data_cleaned

#data preprocessing for diabetes data
#print(data_d.isnull().sum())
#print(data_d.columns)








