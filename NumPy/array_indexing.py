import numpy as np
arr0=np.array(50)
arr1=np.array([1,2,3,4])
arr2=np.array([[1,2,3,4],[4,5,8,6]])
arr3=np.array([[[1,5,6],[2,5,7]],[[3,6,4],[4,5,2]]])


# access 1-D array element

'''
Get third and fourth elements from the  arr1 and add them
'''
print(arr1[2]+arr1[3])

# access 2-D array element

'''
Access the element on the first row, second column for arr2 
'''

print(arr2[0,1])

# Access 3-D array element

'''
Access the third element of the second array of the first array for arr3
'''

print(arr3[0,1, -2])