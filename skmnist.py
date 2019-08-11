import pandas as pd
import tensorflow as tf



train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

labels = train_data["label"]
features = train_data[train_data.columns[1:]].values/255
test = test_data.values/255

train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"pixels": features},
        y=labels,
        batch_size=100,
        num_epochs=3,
        shuffle=True)
feature_columns = [tf.feature_column.numeric_column("pixels", shape=784)]
classifier = tf.estimator.LinearClassifier(
                feature_columns=feature_columns,
                n_classes=10
                )
classifier.train(input_fn=train_input_fn)

predict_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'pixels': test},
        batch_size=1,
        num_epochs=1,
        shuffle=False)
predictions = classifier.predict(input_fn=predict_input_fn)

predicted_classes = [int(prediction['classes'][0]) for prediction in predictions]
index = list(range(1,28001))
pd.DataFrame({"ImageId":index,"Label":predicted_classes}).to_csv("data/sample_submission.csv",index=False)
