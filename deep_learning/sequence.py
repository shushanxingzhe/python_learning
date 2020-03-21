import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(8, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1), name='MyConv2D',
                           padding='same'),
    tf.keras.layers.MaxPool2D(strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(10, activation='softmax')
])


# Take a look at the model summary
# tf.keras.utils.plot_model(model)
model.summary()
model.compile(optimizer='rmsprop', loss=tf.keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])


def decay(epoch):
    if epoch < 3:
        return 1e-3
    elif 3 <= epoch < 7:
        return 1e-4
    else:
        return 1e-5


callbacks = [
    tf.keras.callbacks.TensorBoard(log_dir="logs"),
    tf.keras.callbacks.LearningRateScheduler(decay),
    tf.keras.callbacks.EarlyStopping(patience=2, monitor='val_loss'),
    tf.keras.callbacks.ModelCheckpoint('./weights/checkpoint.h5', load_weights_on_restart=True, mode='auto', save_freq=2000),
]
history = model.fit(x_train, y_train, epochs=5, callbacks=callbacks)
model.summary()
# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['loss'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

model.evaluate(x_test, y_test)

model.save('./weights/my_modelnew.h5')

plt.show()


