
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([10,15,25,9,4,8,14,6])
plt.show()

# Plotting a Displot Without the Histogram

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()

# Normal (Gaussian) Distribution

'''
It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.
'''

x= np.random.normal(size=(2,3))
print(x)
y= np.random.normal(loc=1,scale=3, size=(2,3))
print(y)

# Visualization of Normal Distribution

sns.displot(np.random.normal(loc=1,scale=2,size=100),kind="kde")
plt.show()

# Binomial Distribution

'''
It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.

'''
biarr= np.random.binomial(n=10,p=.5,size=10)
print(biarr)
sns.displot(biarr)
plt.show()

# Difference Between Normal and Binomial Distribution

data={
    "normal": np.random.normal(loc=50, scale=5,size=1000),
    "binormal":np.random.binomial(n=100,p=0.5,size=1000)
}

print(data)
sns.displot(data,kind="kde")
plt.show()

