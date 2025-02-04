import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd

diabetes_data = pd.read_csv("/home/kev-man/Models/Datasets/archive (2)/diabetes_data_upload.csv")

#data preprocessing

def remove_empty_rows_columns(df):
    df_cleaned_rows = df.dropna(how='all')
    df_cleaned = df_cleaned_rows.dropna(axis=1, how='all')
    
    return df_cleaned

diabetes_data_cleaned = remove_empty_rows_columns(diabetes_data)
clean= diabetes_data.drop(columns=["Obesity","Gender","partial paresis","muscle stiffness"])





#print(clean.head())
print(clean)