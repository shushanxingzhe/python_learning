import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x = np.linspace(1,100)

y1 = 1 / x
y2 = np.exp(-((x-50)**2)/50)
y3 = 1 / (101-x)

stage = ['Stage3', 'Stage2', 'Stage1']
level = ['Good', 'Middle', 'Bad']

for i in range(3):
    for j in range(3):
        plt.subplot(331 + (3*i + j))
        plt.plot(x,eval('y' + str(j+1)))
        if j == 0:
            plt.ylabel(stage[i])
        if i == 2:
            plt.xlabel(level[j])

plt.show()