from keras import layers
from keras.models import Model

x = layers.Input((1024,1024,3))
branch_a = layers.Conv2D(128, 1,activation='relu', strides=2, padding='same', name='branch_a')(x)

branch_b = layers.Conv2D(128, 1, activation='relu')(x)
branch_b = layers.Conv2D(128, 3, activation='relu', strides=2, padding='same')(branch_b)

branch_c = layers.AveragePooling2D(3, strides=2, padding='same')(x)
branch_c = layers.Conv2D(128, 3, activation='relu', padding='same')(branch_c)

branch_d = layers.Conv2D(128, 1, activation='relu', name='branch_d')(x)
branch_d = layers.Conv2D(128, 3, activation='relu', padding='same')(branch_d)
branch_d = layers.Conv2D(128, 3, activation='relu', strides=2, padding='same')(branch_d)
output = layers.concatenate([branch_a, branch_b, branch_c, branch_d], axis=-1)

model = Model(x,output)
model.summary()

# share layer
from keras import layers
from keras import applications
from keras import Input
vgg16_base = applications.vgg16.VGG16(weights=None,include_top=False)
left_input = Input(shape=(250, 250, 3))
right_input = Input(shape=(250, 250, 3))
left_features = vgg16_base(left_input)
right_input = vgg16_base(right_input)
merged_features = layers.concatenate([left_features, right_input], axis=-1)


# RESIDUAL
from keras import layers
x = layers.Input((512,512,3))
y = layers.Conv2D(128, 3, activation='relu', padding='same')(x)
y = layers.Conv2D(128, 3, activation='relu', padding='same')(y)
y = layers.MaxPooling2D(2, strides=2)(y)
residual = layers.Conv2D(128, 1, strides=2, padding='same')(x)
y = layers.add([y, residual])