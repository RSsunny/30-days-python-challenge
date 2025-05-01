import numpy as np

arr1=np.array([1,2,3,4,5,6,1,4,3,2,4,1,5,6,8,7,4,5,8,6,5,4,7,8,2,5,4,1,5,3,4])
print(np.where(arr1==3))
print(np.searchsorted(arr1,4))