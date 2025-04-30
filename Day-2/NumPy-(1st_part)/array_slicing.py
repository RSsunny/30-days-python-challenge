import numpy as np

arr1= np.array([1,2,3,4,5,6,7,9])
print(arr1[1:5])

# Slice elements from index 2 to the end of the array:
print(arr1[2:])

# Slice elements from the beginning to index 4 (not included)

print(arr1[:4])

# Slice from the index 3 from the end to index 1 from the end

print(arr1[-3:-1])

# STEP  1-Dimension
print(arr1[1:5:3])