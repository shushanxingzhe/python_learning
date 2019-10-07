import tensorflow as tf
import numpy as np
import tensorflow.keras.backend as K
import os
import requests


def save_model_to_serving(model, export_version, export_path='prod_models'):
    print(model.input, model.output)
    signature = tf.saved_model.signature_def_utils.predict_signature_def(
        inputs={'x1': model.input[0],'x2': model.input[1]}, outputs={'main_output': model.output})
    export_path = os.path.join(
        tf.compat.as_bytes(export_path),
        tf.compat.as_bytes(str(export_version)))
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    legacy_init_op = tf.group(tf.tables_initializer(), name='legacy_init_op')
    builder.add_meta_graph_and_variables(
        sess=K.get_session(),
        tags=[tf.saved_model.tag_constants.SERVING],
        signature_def_map={
            tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature,
        },
        legacy_init_op=legacy_init_op)
    builder.save()


train_x1 = np.linspace(1,1000,1000)
train_x2 = np.linspace(10,2000,1000)

labels = train_x1 * (train_x2 + train_x1)

x1 = tf.keras.layers.Input(shape=1, name='x1')
x2 = tf.keras.layers.Input(shape=1, name='x2')

xtmp = tf.keras.layers.add([x1, x2])
main_output = tf.keras.layers.multiply([x1, xtmp],name='main_output')

model = tf.keras.Model(inputs=[x1, x2], outputs=[main_output])

model.summary()
model.compile(optimizer='adam', loss=tf.keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])


def decay(epoch):
    if epoch < 3:
        return 1e-3
    elif 3 <= epoch < 7:
        return 1e-4
    else:
        return 1e-5


result = model.predict({'x1':np.array([3000]),'x2':np.array([321])})
print(result)

export_path = "export_model"
save_model_to_serving(model, "1", export_path)


'''
run tensorflow serving
docker run -t --rm -p 8501:8501 \
    -v "/e/research/learn/tensorf/export_model/:/models/fashion_mnist" \
    -e MODEL_NAME=fashion_mnist \
    tensorflow/serving &
'''
'''
url = 'http://192.168.99.100:8501/v1/models/learn:predict'

d = {"instances": [{"x1":100,"x2":456}]}
res = requests.post(url, json=d)

print(res.text)
'''






