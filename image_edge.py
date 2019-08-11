import numpy as np
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt


def detect_edges(image,masks):
    edges=np.zeros(image.shape)
    for mask in masks:
        edges=np.maximum(scipy.ndimage.convolve(image, mask), edges)
    return edges

image=plt.imread("dog.jpg")
from skimage import color
gimg = color.colorconv.rgb2grey(image)

Faler= [[
    # [3,0,-3],
    # [10,0,-10],
    # [3,0,-3]
    [3,0,-3],
    [3,0,-3],
    [3,0,-3]],

    [[-3,0,3],
    [-3,0,3],
    [-3,0,3]],

    [[0,3,0],
    [-3,0,3],
    [0,-3,0]],

    [[0,3,0],
    [3,0,-3],
    [0,-3,0]],
]
Faler1= [
    [0,3,0],
    [-3,0,3],
    [0,-3,0]
   ]



edges=detect_edges(gimg, Faler)
#edges1=detect_edges(gimg, Faler1)

fig = plt.gcf()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
#ax3 = fig.add_subplot(133)
ax1.imshow(gimg)
ax2.imshow(edges)
#ax3.imshow(edges1)
plt.show()