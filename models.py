import pandas as pd
from mymodules import *
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree




features= data_cleaned[['Age','Height','Weight','BMI']]
labels=data_cleaned['ObesityCategory']

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.5,random_state=42)

label_encoder = LabelEncoder()

labels_train_encoded = label_encoder.fit_transform(labels_train)
labels_test_encoded = label_encoder.transform(labels_test)

model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(features_train,labels_train_encoded)
predictions=model.predict(features_test)
accuracy=accuracy_score(labels_test_encoded,predictions)


joblib.dump(model, 'obesity_prediction.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
print("Label Encoder Classes:", label_encoder.classes_)  # Debugging
print(data_cleaned.head(12))

#visuals
feature_importances = model.feature_importances_
feature_names = features.columns

# feature importance
plt.figure(figsize=(8,5))
sns.barplot(x=feature_importances, y=feature_names, palette="viridis")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Feature Importance in Obesity Prediction Model")
plt.show()

# Decision Tree visualization
plt.figure(figsize=(15,10))
plot_tree(model.estimators_[0], feature_names=features.columns, class_names=label_encoder.classes_, filled=True, rounded=True)
plt.show()
