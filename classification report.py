#classification report
#an investment company plans to invest in different based on various features and parameters of the startup.
#the company plans to classify the startups as 0 and 1,0 for noninvestable startups and 1 for the investable startups.
#you are provided with training and testing data as inputs.fit a logistic regression model using the training data.
#once fitted,return the classification report on the test data for the fitted logistic regression model.
 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def Classification_report(X_train,y_train,X_test,y_test):
    #fitting the logistic regression model using the training data
    model = LogisticRegression()
    model.fit(X_train,y_train)
    #predicting the test data using the fitted model
    y_pred = model.predict(X_test)
    #returning the classification report on the test data
    return classification_report(y_test,y_pred)    
    
#exaple1
X_train=[[13.2],[15.2],[17.5],[19.9],[15],[19.4]]
X_test=[[13.2],[22.5],[14.3],[22.9]]
y_train=[0,1,0,1,0,1]
y_test=[0,0,0,1]
print(Classification_report(X_train,y_train,X_test,y_test))

#example2
X_train=[[9,3,3],[8,3,1],[9,9,9],[9,4,9],[8,7,7],[6,7,6]]
X_test=[[2,6,2],[2,5,0],[4,3,1],[9,9,8]]
y_train=[0,0,1,1,1,1]
y_test=[0,0,0,1]
print(Classification_report(X_train,y_train,X_test,y_test))





