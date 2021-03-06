# X = [
#     ['Young', 'No Work', 'No House', 'Credit'],
#     ['Young', 'No Work', 'No House', 'Good Credit'],
#     ['Young', 'Have Work', 'No House', 'Good Credit'],
#     ['Young', 'Have Work', 'Have House', 'Credit'],
#     ['Young', 'No Work', 'No House', 'Credit'],
#
#     ['Middle age', 'No Work', 'No House', 'Credit'],
#     ['Middle age', 'No Work', 'No House', 'Good Credit'],
#     ['Middle age', 'Yes Work', 'Have House', 'Good Credit'],
#     ['Middle age', 'No Work', 'Have House', 'Very Good Credit'],
#     ['Middle age', 'No Work', 'Have House', 'Very Good Credit'],
#
#     ['Old age', 'No Work', 'Have House', 'Very Good Credit'],
#     ['Old age', 'No Work', 'Have House', 'Good Credit'],
#     ['Old age', 'Have Work', 'No House', 'Good Credit'],
#     ['Old age', 'Have Work', 'No House', 'Very Good Credit'],
#     ['Old age', 'No Work', 'No House', 'Credit'],
# ]
#
X = [
    [1, 0, 0, 1],
    [1, 0, 0, 2],
    [1, 1, 0, 2],
    [1, 1, 1, 1],
    [1, 0, 0, 1],

    [2, 0, 0, 1],
    [2, 0, 0, 2],
    [2, 1, 1, 2],
    [2, 0, 1, 3],
    [2, 0, 1, 3],

    [3, 0, 1, 3],
    [3, 0, 1, 2],
    [3, 1, 0, 2],
    [3, 1, 0, 3],
    [3, 0, 0, 1],
     ]
Y = [0, 0,1,1,0,0,0,1,1,1,1,1,1,1,0]
#
# from sklearn import tree
# import matplotlib.pyplot as plt
# clf = tree.DecisionTreeClassifier()
# clf.fit(X,Y)
#
# tree.plot_tree(clf)
# plt.show()

import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt

dtest = np.array([[1, 0, 1, 1], [2, 0, 1, 3]])

model = xgb.XGBClassifier()
model.fit(np.array(X), Y)
preds = model.predict(dtest)

print(preds)

dtrain = xgb.DMatrix(np.array(X), label=np.array(Y))
dtest = xgb.DMatrix(dtest)

params = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}

bst = xgb.train(params, dtrain, 2)
result = bst.predict(dtest)
print(result)

xgb.plot_tree(model)
xgb.plot_tree(bst)
plt.show()