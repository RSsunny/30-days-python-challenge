import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = np.array([1, 2, 3, 4])
y = np.array([4, 9, 6, 7])

# normal Python build-in method
z=[]
for i,j in zip(x,y):
    z.append(i+j)

print(z)

# ufunction method add() function

newArr= np.add(x,y)
print(newArr)

# Subtraction
print(np.subtract(x,y))
# Multiplication
print(np.multiply(x,y))
# Division
print(np.divide(x,y))
# Power
print(np.power(x,y))
# Remainder

print(np.remainder(x,y))

# Absolute Values
arr= np.array([-5,2,6,8,-5,-9,-8,9,-7])
print(np.absolute(arr))
