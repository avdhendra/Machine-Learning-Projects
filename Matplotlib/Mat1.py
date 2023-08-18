import matplotlib.pyplot as plt
import numpy as np

x=np.arange(10)
y1=x**2
y2=2*x+3
plt.plot(x,y1,color="red",label="car",linestyle="dashed")
plt.xlabel("time")
plt.ylabel("distance")
plt.show()


prices=np.array([1,2,3,4,5])**3
plt.plot(prices) # here x is index of the array and y is the array
plt.show()