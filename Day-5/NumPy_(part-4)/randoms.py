from numpy import random

x = random.randint(100)
y= random.rand()
arr= random.randint(100,size=(5,3))
arr2= random.rand(5)
print(arr)
print(arr2)
print(random.choice(arr2))

# Random Data Distribution
print(random.choice([4,5,6,7,2],p=[0.3,0.5,0.1,0.1,0.0],size=100))
#