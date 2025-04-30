import numpy as np
from numpy.ma.core import concatenate

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arrJoin= np.concatenate((arr1,arr2))
print(arrJoin)

# Join two 2-D arrays along rows (axis=1):
arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

x= np.concatenate((arr3,arr4),axis=1)
print(x)

# Joining Arrays Using Stack Functions

arr4 = np.array([[1, 2], [3, 4]])

arr5 = np.array([[5, 6], [7, 8]])
y=np.stack((arr4,arr5),axis=1)
print("Stack :",y)

# NumPy provides a helper function: hstack() to stack along rows.

print( "Hstack :" , np.hstack((arr1,arr2)))