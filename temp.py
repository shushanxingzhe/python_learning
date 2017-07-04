import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,500)
y = np.log(1+np.exp(x))
plt.plot(x,y)
plt.show()
