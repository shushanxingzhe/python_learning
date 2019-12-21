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
    print('label:',label,'\tpredict:',resp['predictions'][0].index(max(resp['predictions'][0])))


# GRPC manner

# coding: utf-8

import numpy as np
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc


def catId_predict(images, batch_size=32):
    """.
    Args:
        images: 数据.
        batch_size: 调用模型预测时的批量数.
    """

    channel = grpc.insecure_channel("192.168.99.100:8501")
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    result = []

    def predict_request(batch_images_features):
        """模型预测请求."""
        images_features_batch = np.asarray(batch_images_features)
        images_tensor_proto = tf.make_tensor_proto(images_features_batch, shape=images_features_batch.shape, dtype=tf.float32)

        try:
            request = predict_pb2.PredictRequest()
            request.inputs["image"].ParseFromString(images_tensor_proto.SerializeToString())
            request.model_spec.name = "fashion_mnist"
            request.model_spec.signature_name = "serving_default"
            response = stub.Predict(request, 10)
            _result = tf.make_ndarray(response.outputs["predictions"]).tolist()
            result.extend([i[0] for i in _result])
        except Exception as e:
            print(e)

    # 批量.
    total = len(images)
    batch_images_features = []
    for i in range(total):
        images_features = images[i]
        batch_images_features.append(images_features)
        if (i + 1) % batch_size == 0:
            predict_request(batch_images_features)
            batch_images_features = []

    if batch_images_features:
        predict_request(batch_images_features)

    channel.close()
    return result

