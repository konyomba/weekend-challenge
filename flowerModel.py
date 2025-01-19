from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#instance of the dataset
Iris= datasets.load_iris()

#preparing and spliting dataset from tarining and testing
features=Iris.data
labels = Iris.target

#creating arrays for training and testing the model

features_test,features_train,labels_test,labels_train=train_test_split(features,labels,test_size=.5)

#training the model

my_classifier=KNeighborsClassifier()
my_classifier.fit(features_train,labels_train)

#passing the test data after training
prediction=my_classifier.predict(features_test)
 
print(accuracy_score(labels_test,prediction))

#the the model by manual input
Iris1 =[[7.5,4.3,5.0,2.4]]
Iris_prediction= my_classifier.predict(Iris1)
if Iris_prediction[0]==0:
    print("Setosa")
if Iris_prediction[0]==1:
    print("Versicolor")
if Iris_prediction[0]==2:
    print("Virginica")

