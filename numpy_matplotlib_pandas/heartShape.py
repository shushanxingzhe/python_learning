import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3.0, 3.0, .01)
y = np.arange(-3.0, 3.0, .01)
x, y = np.meshgrid(x, y)

f = -x**2 * y**3 + (x**2 + y**2 -1)**3
plt.figure()
plt.contour(x, y, f, 0,)
plt.show()
