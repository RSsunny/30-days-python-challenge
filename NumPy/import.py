import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1)

print(np.__version__)

print(type(arr1))
arr2 = np.array((1,2,3,4,5,6,7))
print(arr2)
print(type(arr2))

'''
dimension of array like one dimension , two dimension , three dimension. 
'''

arr3= np.array(50)
arr4= np.array([1,2,3])
arr5= np.array([[1,2,3],[4,5,6]])
arr6= np.array([[[1,2,3],[5,1,4]],[[4,5,4],[5,4,1]]])
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
print(arr6.ndim)
