from mymodules import *
import pandas as pd
from mymodules import *
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

features = cleanD_data[['weight','height','blood_glucose','medication_adherence','bmi']]

labels = cleanD_data['risk_score']

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.5,random_state=42)



print(set(labels_train))
print(cleanD_data.head(10))