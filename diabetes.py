
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  
from mymodules import *




categorical_cols = ["Gender", "Polyuria", "Polydipsia", "sudden weight loss", "weakness", 
                    "Polyphagia", "Genital thrush", "visual blurring", "Itching", "Irritability", 
                    "delayed healing", "partial paresis", "muscle stiffness", "Alopecia", "Obesity"]

label_encoder = LabelEncoder()
for col in categorical_cols:
    data_d[col] = label_encoder.fit_transform(data_d[col])


data_d['class'] = label_encoder.fit_transform(data_d['class'])


X = data_d.drop(columns=['class'])  
y = data_d['class']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train['Age'] = scaler.fit_transform(X_train[['Age']])
X_test['Age'] = scaler.transform(X_test[['Age']])


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix Visualization
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


joblib.dump(model, "diabetes_model.pkl")

