from keras.datasets import reuters
(train_data, train_labels),(test_data,test_labels) = reuters.load_data(num_words=10000)

word_index = reuters.get_word_index()
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])

def decode_text(data):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in data])
print(decode_text(train_data[0]))

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

from keras.utils import to_categorical
one_hot_train_labels = to_categorical(train_labels,num_classes=46)
one_hot_test_labels = to_categorical(test_labels,num_classes=46)

input = layers.Input(shape=(10000,))
output = layers.Dense(64,activation='relu')(input)
output = layers.Dense(64,activation='relu')(output)
output = layers.Dense(46,activation='softmax')(output)
model = models.Model(input=input,output=output)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,one_hot_train_labels,epochs=9,batch_size=512)
result = model.evaluate(x_test,one_hot_test_labels)
print(result)


# sparse_categorical_crossentropy
input = layers.Input(shape=(10000,))
output = layers.Dense(64,activation='relu')(input)
output = layers.Dense(64,activation='relu')(output)
output = layers.Dense(46,activation='softmax')(output)
sparse_model = models.Model(input=input,output=output)
sparse_model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


sparse_model.fit(x_train,y_train,epochs=9,batch_size=512)
result = sparse_model.evaluate(x_test,y_test)
print(result)


text = decode_text(test_data[9])
print(text)
pred_y = sparse_model.predict(x_test)
print(np.argmax(pred_y[9]))
print(y_test[9])
