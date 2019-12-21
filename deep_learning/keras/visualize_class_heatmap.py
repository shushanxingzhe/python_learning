from keras.applications import VGG16
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import cv2
import os

model = VGG16(weights='imagenet')

model.summary()

img_path = '../../data/snail.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

class_idx = np.argmax(preds[0])

image_output = model.output[:, class_idx]
last_conv_layer = model.get_layer('block5_conv3')

grads = K.gradients(image_output, last_conv_layer.output)[0]
pooled_grads = K.mean(grads, axis=(0, 1, 2))
iterate = K.function([model.input],
                     [pooled_grads, last_conv_layer.output[0]])
pooled_grads_value, conv_layer_output_value = iterate([x])
for i in range(512):
    conv_layer_output_value[:, :, i] *= pooled_grads_value[i]
heatmap = np.mean(conv_layer_output_value, axis=-1)

heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
plt.matshow(heatmap)
plt.show()

img = cv2.imread(img_path)
heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
superimposed_img = heatmap * 0.4 + img
cam_image = 'image_cam.jpg'
cv2.imwrite(cam_image, superimposed_img)
cam = plt.imread(cam_image)
plt.imshow(cam)
plt.show()

os.remove(cam_image)
