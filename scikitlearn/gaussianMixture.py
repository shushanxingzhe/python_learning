import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn import mixture

x = np.linspace(-5,10,1000)[:, np.newaxis]


dense = (0.3 * norm(0,1).pdf(x[:,0]) + 0.7 * norm(5,1).pdf(x[:,0]))[:, np.newaxis]

plt.fill(x[:,0],dense,fc="black", alpha=0.3)
N = 100
np.random.seed(1)
X = np.concatenate((np.random.normal(0,1,int(0.3 * N)),np.random.normal(5,1,int(0.7*N))))[:, np.newaxis]


model = KernelDensity(kernel='gaussian',bandwidth=0.6)
kde = model.fit(X)

y_smp = kde.score_samples(x)
plt.plot(x,np.exp(y_smp))


clf = mixture.GaussianMixture(n_components=2, covariance_type='full')
clf.fit(X)
tmp = clf._get_parameters()
print(tmp)


plt.show()