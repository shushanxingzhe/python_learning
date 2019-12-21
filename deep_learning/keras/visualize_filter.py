from keras.applications import VGG16
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

model = VGG16(weights='imagenet', include_top=False)

model.summary()


def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1
    x += 0.5
    x = np.clip(x, 0, 1)
    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x


def generate_pattern(layer_name, filter_index, size=150):
    layer_output = model.get_layer(layer_name).output
    loss = K.mean(layer_output[:, :, :, filter_index])
    grads = K.gradients(loss, model.input)[0]
    grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)
    iterate = K.function([model.input], [loss, grads])
    input_img_data = np.random.random((1, size, size, 3)) * 20 + 128.
    step = 1.
    for i in range(40):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * step
        img = input_img_data[0]
    return deprocess_image(img)


plt.imshow(generate_pattern('block3_conv1', 0))


def visualize_layer(layer_name, number=4, size=64):
    margin = 3
    results = np.zeros((number * size + (number-1) * margin, number * size + (number-1) * margin, 3), dtype=int)
    for i in range(number):
        for j in range(number):
            filter_img = generate_pattern(layer_name, i + (j * number), size=size)
            horizontal_start = i * size + i * margin
            horizontal_end = horizontal_start + size
            vertical_start = j * size + j * margin
            vertical_end = vertical_start + size
            results[horizontal_start: horizontal_end, vertical_start: vertical_end, :] = filter_img

    plt.figure()
    plt.imshow(results)


visualize_layer('block1_conv1',3,64)
visualize_layer('block2_conv1',3,64)
visualize_layer('block3_conv1',3,64)
visualize_layer('block4_conv1',3,64)
visualize_layer('block5_conv1',3,64)

plt.show()
