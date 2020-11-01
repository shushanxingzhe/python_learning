import copy

import matplotlib.pyplot as plt
import numpy as np


class Kmeans(object):
    def __init__(self, max_step=1000, min_move=0.01):
        self.max_step = max_step
        self.min_move = min_move

    def fit(self, train, k):
        center_idx = np.random.choice(len(train), k)
        center = train[center_idx]
        move = 1000
        step = 0
        distance = np.zeros((len(train), k))
        labels = np.zeros(len(train))
        while move > self.min_move and step < self.max_step:
            for i in range(k):
                distance[:, i] = np.sqrt(np.sum(np.square(train - center[i]), axis=-1))
            labels = np.argmin(distance, axis=-1)
            pre_center = copy.deepcopy(center)
            for i in range(k):
                center[i] = np.mean(train[labels == i], axis=0)
            move = np.mean(np.sqrt(np.sum(np.square(center - pre_center))))
            step += 1
        return labels


c1 = np.random.randn(200, 2) + [1, 1]
c2 = np.random.randn(200, 2) + [6, 3]
c3 = np.random.randn(200, 2) + [4, 7]
data = np.concatenate([c1, c2, c3], axis=0)

model = Kmeans()
label = model.fit(data, 3)
plt.scatter(data[:, 0], data[:, 1], c=label)
plt.show()
