from scipy.interpolate import lagrange
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = 1.5 * x**3 + 5.1*x**2 - 3*x +7
print(y)
y = y + np.random.randn(len(x))
print(y)
poly = lagrange(x, y)

from numpy.polynomial.polynomial import Polynomial
coefs = Polynomial(poly).coef
print(coefs)
for index,coef in enumerate(coefs):
    if coef < 0.01:
        coefs[index] = 0

print(coefs)
newPoly = np.poly1d(coefs)

print(poly(1))
print(poly(5))
print(newPoly(1))
print(newPoly(5))
print('lagrange对现有数据拟合好，同时严重过拟合，泛化效果差')
print('==============================================================================================================')

from scipy import linalg
import numpy as np

#Declaring the numpy arrays
coef = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
y = np.array([2, 4, -1])

#Passing the values to the solve function
x = linalg.solve(coef, y)
#printing the result array
print(x)




A = np.array([[1,2],[3,4]])
#Passing the values to the det function
x = linalg.det(A)
#printing the result
print(x)



#Declaring the numpy array
A = np.array([[1,2],[3,4]])
#Passing the values to the eig function
l, v = linalg.eig(A)
#printing the result for eigen values
print(l)
#printing the result for eigen vectors
print(v)



# 奇异值分解（SVD）可以被认为是特征值问题扩展到非矩阵的矩阵。
# 所述 scipy.linalg.svd 因子分解矩阵“A”成两个酉矩阵“U”和“VH”和奇异值（真实的，非负）这样的一个1-d阵列的'一个==ù S Vh，
# 其中'S'是具有主对角线's'的适当形状的零点矩阵。

#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)
#Passing the values to the eig function
U, s, Vh = linalg.svd(a)
# printing the result
print (U, Vh, s)


from scipy.fftpack import fft,ifft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print(y)
yinv = ifft(y)
print(yinv)
