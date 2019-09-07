import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

labels = train_data["label"]
features = train_data[train_data.columns[1:]].values/255


test = test_data.values/255

model = LogisticRegression()
model.fit(features,labels)
predictions = model.predict(test)

index = list(range(1,28001))
pd.DataFrame({"ImageId":index,"Label":predictions}).to_csv("data/evaluation_submission_svm.csv",index=False)
