from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV,cross_val_score

iris = datasets.load_iris()
parameters = {'kernel': ['linear', 'rbf'], 'C': [1, 10]}
svc = svm.SVC(gamma="scale")
clf = GridSearchCV(svc, parameters, cv=5)
clf.fit(iris.data, iris.target)
print(clf.cv_results_)



scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
