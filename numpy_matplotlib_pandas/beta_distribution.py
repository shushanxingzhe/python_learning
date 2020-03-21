import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

x = np.linspace(0, 1.0, 100)


y1 = beta.pdf(x, 40,60)
y2 = beta.pdf(x, 40+20,60+20)
plt.plot(x, y1, "r--",x,y2,'g-.')
plt.show()