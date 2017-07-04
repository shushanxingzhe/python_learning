
import numpy as np
import matplotlib.pyplot as plt

a = 1
t = np.linspace(0 , 2 * np.pi, 1024)
X = a*(2*np.cos(t)-np.cos(2*t))
Y = a*(2*np.sin(t)-np.sin(2*t))
plt.plot(Y, X,color='r')
plt.show()

def pdf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X - mu) ** 2)
X = np.linspace(-6, 6, 1000)
for i in range(3):
    samples = np.random.standard_normal(10)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(X, pdf(X, mu, sigma), color = '.66')
plt.plot(X, pdf(X, 0., 1.), color = 'b')
plt.show()

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
plt.title('$f(x)=\\frac{1}{4}(x+4)(x+1)(x-2)$')
plt.plot(X, Y, c = 'g')
plt.show()

X = np.linspace(0, 2 * np.pi, 100)
YSinValues = np.sin(X)
YCosValues = np.cos(X)
plt.plot(X, YSinValues)
plt.plot(X, YCosValues)
plt.show()

