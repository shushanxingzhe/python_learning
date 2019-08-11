import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,500)
y = np.log(1+np.exp(x))
plt.plot(x,y)
plt.show()

import keras
x = [3,4,8,1,3]
y = keras.utils.normalize(x, axis=-1, order=2)
print(y)