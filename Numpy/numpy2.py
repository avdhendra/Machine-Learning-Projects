'''
Numpy random module
rand: Random value in a given shape
randn:return a sample(or samples) from the standard normal distribution
randint:return random integers from low(inclusive) to high(exclusive)
random:return random float in the half opne interval[0.0,1.0)
choice:Generates a random smaple from a given 1-D Array
Shuffle:Shuffles the contents of a sequence



'''
import numpy as np


a=np.arange(10)+5
print(a)

a=np.random.randn(2,3)
