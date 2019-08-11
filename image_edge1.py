from numpy import *
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

def detect_edges(image,masks):
    edges=zeros(image.shape)
    for mask in masks:
        edges=maximum(scipy.ndimage.convolve(image, mask), edges)
    return edges

image=plt.imread("dog.jpg")
from skimage import color
gimg = color.colorconv.rgb2grey(image)

Faler=[ [[-1,0,1],[-1,0,1],[-1,0,1]],
        [[1,1,1],[0,0,0],[-1,-1,-1]],
    [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],
    [[0,1,0],[-1,0,1],[0,-1,0]] ]

edges=detect_edges(gimg, Faler)
plt.imshow(edges)
plt.show()