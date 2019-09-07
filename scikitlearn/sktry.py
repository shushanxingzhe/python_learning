import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures



features = np.linspace(1,50).reshape(-1, 1)

labels = features ** 2
print(features)
print(labels)

test = np.reshape([5,10,15,18,100],[-1, 1])
print(test)

quadratic_featurizer = PolynomialFeatures(degree=2)
features = quadratic_featurizer.fit_transform(features,labels)
test = quadratic_featurizer.transform(test)


model = LogisticRegression()
model.fit(features,labels)
predictions = model.predict(test)

print(predictions)


