import nni
import xgboost
from sklearn.metrics import f1_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def get_default_param():
    return {'learning_rate': 0.01, 'max_depth': 5, 'reg_alpha': 0.4, 'reg_lambda': 0.6}


def train(params):
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=7, test_size=0.25)

    model = xgboost.XGBClassifier(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    nni.report_final_result(f1_score(y_test, y_pred, average='macro'))


if __name__ == '__main__':
  params = get_default_param()
  params.update(nni.get_next_parameter())
  train(params)

# nnictl create --config config.yml
