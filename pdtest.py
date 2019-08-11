import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("data/small.csv")

labels = data["label"]
#features = data[data.columns[1:]].values/255
features = data.iloc[:,1:].values/255
test = data.values/255
print(features.shape)


for i in range(1,10):
    #img = np.reshape(data.loc[i][1:].values / 255,(28,28))
    img = np.reshape(features[i] / 255,(28,28))

    plt.figure()
    plt.title(data.loc[i][0])
    plt.imshow(img)

plt.show()
