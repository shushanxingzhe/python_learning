import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

a = [1,2,3,4,5,6]
print(a[:-2])
print(a[2:])
tf.keras.layers.Embedding()
exit()

tf.enable_eager_execution()

tf.logging.set_verbosity(tf.logging.ERROR)
tf.set_random_seed(123)

# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tfbt/titanic_train.csv')
dfeval = pd.read_csv('https://storage.googleapis.com/tfbt/titanic_eval.csv')
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

dftrain['class'].value_counts().plot(kind='barh')

fc = tf.feature_column
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']


def one_hot_cat_column(feature_name, vocab):
  return fc.indicator_column(fc.categorical_column_with_vocabulary_list(feature_name, vocab))


feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  # Need to one-hot encode categorical features.
  vocabulary = dftrain[feature_name].unique()
  feature_columns.append(one_hot_cat_column(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(fc.numeric_column(feature_name, dtype=tf.float32))

example = dftrain.head(1)
class_fc = one_hot_cat_column('class', ('First', 'Second', 'Third'))
print('Feature value: "{}"'.format(example['class'].iloc[0]))
print('One-hot encoded: ', fc.input_layer({'class': pd.Series(['Second'])}, [class_fc]).numpy())


tf.data.Dataset.from_tensor_slices()
tf.keras.preprocessing.image.ImageDataGenerator()
tf.keras.layers.Lambda()
plt.subplot()

tf.keras.applications.vgg19.VGG19()
tf.nn.rnn_cell.MultiRNNCell()
tf.estimator.Estimator()
tf.keras.Model()
tf.estimator.DNNClassifier()
tf.layers.dense()

tf.train.shuffle_batch()
