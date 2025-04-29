import numpy as np

arr1= np.array([1,2,3,4,5,6,7,8,9])
# 1-Dimension to 2-dimension
x= arr1.reshape(3,3)
print(x)

# 1-dimension to 3-dimension
arr2= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y= arr2.reshape(2,3,2)
print(y)
# array add
arr3= np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
z= arr3.reshape(-1)
print(z)