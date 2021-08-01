import xgboost
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


X_train = np.linspace(5, 10, 20)
X_train = X_train.reshape((-1, 1))
y_train = 0.2 * X_train ** 2 + 3
X_test = np.linspace(15, 20, 20)
X_test = X_test.reshape((-1, 1))
y_test = 0.2 * X_test ** 2 + 3

model = xgboost.XGBRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(r2_score(y_test, y_pred))

plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_pred)
plt.plot(X_test, y_test)


model = xgboost.XGBRegressor(booster='gblinear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(r2_score(y_test, y_pred))
plt.subplot(1, 2, 2)
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_pred)
plt.plot(X_test, y_test)
plt.show()
