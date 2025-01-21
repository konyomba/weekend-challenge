import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('/home/kev-man/Datasets/archive/obesity_data.csv')
data= data.drop(columns="PhysicalActivityLevel")

data_cleaned= data
def clean_row(data):
    data_cleaned = data.dropna()
    return data_cleaned



features= data_cleaned[['Age','Gender','Height','Weight','BMI']]
labels=data_cleaned['ObesityCategory']

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.5,random_state=42)

label_encoder = LabelEncoder()
features_train['Gender'] = label_encoder.fit_transform(features_train['Gender'])
features_test['Gender'] = label_encoder.transform(features_test['Gender'])
labels_train_encoded = label_encoder.fit_transform(labels_train)
labels_test_encoded = label_encoder.transform(labels_test)

model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(features_train,labels_train_encoded)
predictions=model.predict(features_test)
accuracy=accuracy_score(labels_test_encoded,predictions)

#print(data_cleaned)
print("Accuracy of model: ",accuracy*100,"%")