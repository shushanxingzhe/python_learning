import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# import autokeras as ak
from tpot import TPOTRegressor


X_train = np.linspace(5, 10, 50)
X_train = X_train.reshape((-1, 1))
y_train = X_train ** 3 + 3
X_test = np.linspace(15, 20, 50)
X_test = X_test.reshape((-1, 1))
y_test = X_test ** 3 + 3

# model = ak.StructuredDataRegressor(overwrite=True, max_trials=3)
# model.fit(X_train, y_train, epochs=10)
model = TPOTRegressor(generations=8, population_size=60, verbosity=2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
model.export('tpot_auto_pipeline.py')

print(r2_score(y_test, y_pred))
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_pred, color='red')
plt.plot(X_test, y_test)
plt.show()



