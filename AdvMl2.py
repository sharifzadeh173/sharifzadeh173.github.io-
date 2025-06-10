
#Create a custom ensemble learning model of Gaussian Naive Bayes, Support Vector Machine, and Random Forest for breast cancer classification task. Obtain the accuracy of this model on a given test size.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def Ensembler(test_size):
    # Load the breast cancer dataset
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target
    # Split the dataset into features and target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Define the models
    gnb = GaussianNB()
    svc = SVC(probability=True)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    # Create the ensemble model
    ensemble = VotingClassifier(estimators=[('gnb', gnb), ('svc', svc), ('rf', rf)], voting='soft')
    #cross validation
    for i in range(10):
        gnb.fit(X_train, y_train)
        svc.fit(X_train, y_train)
        rf.fit(X_train, y_train)        
         
    # Train the ensemble model
    ensemble.fit(X_train, y_train)
    # Make predictions on the test set
    y_pred = ensemble.predict(X_test)
    # Calculate the accuracy of the ensemble model
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Driver Code
#Example 1:

#Input

test_size = 0.3
print(Ensembler(test_size))
#Output
#0.959
#Example 2:
#Input

test_size = 0.25
print(Ensembler(test_size))
#Output
#0.965
#Constraints
#- Use 'load_breast_cancer' from sklearn Dataset module. - Set random_state=42 when making training and test sets.