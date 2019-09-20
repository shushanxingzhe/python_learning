import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

n_data = 1000
seed = 1
n_clusters = 4
n_centers = 4

# 产生高斯随机数，运行K-均值
blobs, blob_labels = make_blobs(n_samples=n_data, n_features=2,centers=n_centers, random_state=seed)

clusters_blob = KMeans(n_clusters=n_centers, random_state=seed).fit_predict(blobs)

# 产生随机数，运行K-均值
uniform = np.random.rand(n_data, 2)
clusters_uniform = KMeans(n_clusters=n_clusters, random_state=seed).fit_predict(uniform)

# 使用Matplotlib进行结果可视化
figure = plt.figure()
plt.subplot(221)
plt.scatter(blobs[:, 0], blobs[:, 1], c=blob_labels, cmap='gist_rainbow')
plt.title("(a) Four randomly generated blobs", fontsize=14)
plt.axis('off')

plt.subplot(222)
plt.scatter(blobs[:, 0], blobs[:, 1], c=clusters_blob, cmap='gist_rainbow')
plt.title("(b) Clusters found via K-means", fontsize=14)
plt.axis('off')

plt.subplot(223)
plt.scatter(uniform[:, 0], uniform[:, 1])
plt.title("(c) 1000 randomly generated points", fontsize=14)
plt.axis('off')

plt.subplot(224)
plt.scatter(uniform[:, 0], uniform[:, 1], c=clusters_uniform, cmap='gist_rainbow')
plt.title("(d) Clusters found via K-means", fontsize=14)
plt.axis('off')
plt.show()