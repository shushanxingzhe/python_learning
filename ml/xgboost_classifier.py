import xgboost
from sklearn.metrics import f1_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=1, test_size=0.25)


model = xgboost.XGBClassifier(objective='multi:softprob', max_depth=5, reg_alpha=0.3, reg_lambda=0.5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f1_score(y_test, y_pred, average='macro'))

xgboost.plot_tree(model.get_booster(), num_trees=0)
xgboost.plot_tree(model.get_booster(), num_trees=1)
xgboost.plot_tree(model.get_booster(), num_trees=2)

plt.show()