#computer vision
#find the accuracy of a random forest classifier given a fixed test size when getting trained on the sklearn Wine Dataset.
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def random_forest_classifier(N):
    wine = load_wine()
    X = wine.data
    y = wine.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = N)
    clf = RandomForestClassifier(n_estimators = 50)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
    

#input
N = .33
#output:    accuracy = 0.9661016949

print(random_forest_classifier(N))
#examle2
N = .4
print(random_forest_classifier(N))

#output:    accuracy = 0.9444444444444444