import numpy as np

arr1= np.array([1,2,3,4])
arr2= np.array([1,2,3,4])
x= arr1.copy()
y=arr2.view()
y[0]=4
x[0]=6

print(arr1)
print(x)
print(arr2)
print(y)