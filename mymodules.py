import pandas as pd


data = pd.read_csv('/home/kev-man/Datasets/archive/obesity_data.csv')
diabetes_data= pd.read_csv('/home/kev-man/Datasets/archive/diabetes_data.csv')
thyroid_data= pd.read_csv('/home/kev-man/Datasets/archive/Thyroid.csv')

diabetes_data = diabetes_data.drop(columns=["user_id","date","stress_level","sleep_hours","diet","hydration_level","physical_activity"])

thyroid_data = thyroid_data.drop(columns=["Pregnancy","Fatigue","Heart_Rate_Changes","Increased_Sweating","Sensitivity_to_Cold_or_Heat","Constipation_or_More_Bowel_Movements","Depression_or_Anxiety","Difficulty_Concentrating_or_Memory_Problems"])

data= data.drop(columns="PhysicalActivityLevel")

data_cleaned= data
def clean_row(data):
    data_cleaned = data.dropna()
    return data_cleaned

cleanD_data = diabetes_data
def clean_row(diabetes_data):
    cleanedD_data = diabetes_data.dropna()
    return cleanD_data

cleanThyroid = thyroid_data
def clean_row(thyroid_data):
    cleanThyroid = thyroid_data.dropna()
    return cleanThyroid

