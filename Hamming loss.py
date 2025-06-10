#Hamming loss
#A medical firm wants to determine whether a person is suffering from a disease X or not(0 or1)based on various features.
#you are provided with X_train, y_train, X_test and y_test as inputs.fit a logistic regression model using the X_train
#and y_train data and obtain predictions for X_test. once predicted ,return the hamming loss
#for the fitted logistic regression model.

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import hamming_loss
def hammingloss(X_train,y_train,X_test,y_test):
    #fit the model
    model=LogisticRegression()
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    #return hamming loss
    return hamming_loss(y_test,y_pred)

#example1
#input:
X_train=[[1,2],[1,3],[1,3],[1,4],[2,3],[6,7]]
X_test=[[1,6],[2,5],[1,3],[2,6]]
y_train=[1,1,0,1,0,0]
y_test=[0,1,1,0]
print(hammingloss(X_train,y_train,X_test,y_test))
#output:.5
#example2:
#input:
X_train=[[1,2,3],[1,3,4],[1,3,2],[1,4,2],[2,3,4],[6,7,6]]
X_test=[[1,6,2],[2,5,6],[1,3,8],[9,2,6]]
y_train=[0,1,0,1,1,1]
y_test=[1,1,1,0]
print(hammingloss(X_train,y_train,X_test,y_test))
#output:.25
#Notice: Hamming loss is the ratio of the number of misclassified samples to the total number of samples.
#less hamming loss is better
    
    
    
