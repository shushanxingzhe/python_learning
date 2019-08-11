import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


model = tf.keras.models.load_model('./weights/my_modelnew.h5')

test_loss, test_acc = model.evaluate(x_test, y_test)
print('test_loss:',test_loss, 'test_acc:', test_acc)
y_pred = model.predict(x_test)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


for i in range(200):
    if np.argmax(y_pred[i]) != y_test[i]:
        plt.imshow(x_test[i].reshape(28,28))
        plt.xlabel(class_names[np.argmax(y_pred[i])])
        plt.ylabel(class_names[y_test[i]],)
        print(class_names[np.argmax(y_pred[i])], '\t', class_names[y_test[i]], '\n')
        plt.show()



