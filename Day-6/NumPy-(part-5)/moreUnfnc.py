import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns
arr= np.random.randint(100,size=100)
# unique
arr2 = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(np.unique(arr2))
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([3, 4, 5, 6])
print( f"union1d : {np.union1d(arr3,arr4)}" )