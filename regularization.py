#regularization
#A fintech company decides to recruit employees. the company holds data of different candidates containing their 
#self_rating on different skils in various domains.the company plans to recruit candidates using machine learning-based
#prediction to classify candidates as 0 and 1. 0 for rejected and 1 for accepted.
#you are provided with the training data and test data as inputs.fit a logistic regression model using data by performing
#regularization,assuming solver='liblinear'.once fitted ,obtain the predictions on the test data for the model. 

from sklearn.linear_model import LogisticRegression
def L1_LogisticRegression(X_train, y_train, X_test, y_test):
    lr = LogisticRegression(penalty = 'l1',solver = 'liblinear')
    lr.fit(X_train, y_train)
    return lr.predict(X_test)
#example1
X_train = [[9,3,3], [8,3,1], [9,9,9], [9,4,9], [8,7,7], [6,7,6]]
y_train = [0, 0,1, 1, 1,1]
X_test = [[2,6,2], [2,5,0], [4,3,1], [9,9,8]]
y_test = [0, 0, 0, 1]
print(L1_LogisticRegression(X_train,y_train,X_test,y_test))
#output:[1,0,0,1]
#example2
X_train = [[10,7,10], [8,3,10], [9,9,9], [9,4,9], [8,7,7], [6,7,6]]
y_train = [1, 0,1, 1, 1,1]
X_test = [[9,10,10], [2,5,0], [4,3,1], [9,9,8]]
y_test = [1, 0, 0, 1]
print(L1_LogisticRegression(X_train,y_train,X_test,y_test))
#output:[1,1,1,1]



