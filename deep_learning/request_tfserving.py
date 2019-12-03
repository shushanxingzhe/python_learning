import requests
import tensorflow as tf
import json

'''
run tensorflow serving
docker run -t --rm -p 8501:8501 \
    -v "/e/research/learn/tensorf/export_model/:/models/fashion_mnist" \
    -e MODEL_NAME=fashion_mnist \
    tensorflow/serving &
'''

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

url = 'http://192.168.99.100:8501/v1/models/fashion_mnist:predict'

for image,label in zip(x_test[0:10],y_test[0:10]):
    image = image.tolist()
    d = {"instances": [{"image":image}]}
    res = requests.post(url, json=d)

    resp = json.loads(res.text)
    print('lable:',label,'\tpredict:',resp['predictions'][0].index(max(resp['predictions'][0])))
