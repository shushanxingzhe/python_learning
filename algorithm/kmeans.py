import matplotlib.pyplot as plt
import numpy as np


class KMeans(object):
    def __init__(self, cluster, max_epoch=100, min_move=0.001):
        self.cluster = cluster
        self.max_epoch = max_epoch
        self.min_move = min_move

    def fit(self, train):
        center_idx = np.random.choice(len(train), self.cluster)
        center = train[center_idx]
        step = 0
        move = 100
        distance = np.zeros((len(train), self.cluster))
        while step < self.max_epoch or move > self.min_move:
            for i in range(self.cluster):
                distance[:, i] = np.sqrt(np.sum(np.square(center[i] - train), axis=-1))
            lables = np.argmin(distance, axis=1)
            pre_center = center
            for i in range(self.cluster):
                center[i] = np.mean(train[lables == i], axis=0)
            move = np.mean(np.sqrt(np.square(center - pre_center)))
            step += 1
        return lables


data1 = np.random.randn(200, 2) + [1, 1]
data2 = np.random.randn(200, 2) + [3, 2]
data3 = np.random.randn(200, 2) + [5, 7]

train = np.concatenate([data1, data2, data3], axis=0)
kmeans = KMeans(3)
lables = kmeans.fit(train)
plt.scatter(train[:, 0], train[:, 1], c=lables)
plt.show()
