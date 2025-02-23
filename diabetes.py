import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


diabetes_data = pd.read_csv("/home/kev-man/Models/Datasets/archive (2)/diabetes_data_upload.csv")

# Convert 'Gender' column to numerical (Male=1, Female=0)
diabetes_data['Gender'] = diabetes_data['Gender'].map({'Male': 1, 'Female': 0})

diabetes_data = diabetes_data.dropna()
print(diabetes_data.isnull().sum())

# Convert 'Yes'/'No' categorical columns to 1/0
binary_cols = diabetes_data.columns[1:-1]  
for col in binary_cols:
    diabetes_data[col] = diabetes_data[col].map({'Yes': 1, 'No': 0})

# Encode 'class' column (Positive = 1, Negative = 0)
diabetes_data['class'] = diabetes_data['class'].map({'Positive': 1, 'Negative': 0})

# Check for missing values
#print("Missing values:\n", diabetes_data.isnull().sum())

# Feature Scaling (Standardization)
scaler = StandardScaler()
X = diabetes_data.iloc[:, :-1]
y = diabetes_data.iloc[:, -1]
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))


joblib.dump(model, "diabetes_model.pkl")
joblib.dump(scaler, "scaler.pkl")

cleaned_file_path = "/home/kev-man/Models/Datasets/cleaned_diabetes_data.csv"
diabetes_data.to_csv(cleaned_file_path, index=False)
#