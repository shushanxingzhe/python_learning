import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 80, normed=True, facecolor='g', alpha=0.75)


x1 = np.linspace(40,160,1000)
y1 = np.exp(-(x1-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
plt.plot(x1,y1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()