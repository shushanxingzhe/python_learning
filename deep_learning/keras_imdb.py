from keras.datasets import imdb
(train_data, train_labels),(test_data,test_labels) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])
decoded_review = ' '.join([reverse_word_index.get(i-3, '?') for i in train_data[0]])
print(decoded_review)

import numpy as np
def vectorize_sequences(sequences, dimension=10000):
    result = np.zeros((len(sequences),dimension))
    for i,sequence in enumerate(sequences):
        result[i,sequence] = 1.
    return result


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
print(x_train[0])
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')
print(y_train[0])

from keras import models
from keras import layers


input = layers.Input(shape=(10000,))
output = layers.Dense(16,activation='relu')(input)
output = layers.Dense(16,activation='relu')(output)
output = layers.Dense(1,activation='sigmoid')(output)
model = models.Model(input=input,output=output)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train,partial_y_train,epochs=20,batch_size=512,validation_data=(x_val,y_val))

print(history.history.keys())

import matplotlib.pyplot as plt
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1,len(loss_values)+1)

plt.plot(epochs,loss_values, 'bo', label='Training loss')
plt.plot(epochs,val_loss_values,'b', label='Validation losss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']

plt.plot(epochs,acc_values, 'bo', label='Training accuracy')
plt.plot(epochs,val_acc_values, 'b', label='Validation accuracy')
plt.title('Training and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()

input = layers.Input(shape=(10000,))
output = layers.Dense(16,activation='relu')(input)
output = layers.Dense(16,activation='relu')(output)
output = layers.Dense(1,activation='sigmoid')(output)
model = models.Model(input=input,output=output)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])


model.fit(x_train,y_train,epochs=4,batch_size=512)
result = model.evaluate(x_test,y_test)
print(result)