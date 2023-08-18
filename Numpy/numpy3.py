'''
Some more numpy functions Statistic
->min,max
->mean,
->median,
->average
->variance
->standard deviation


'''
import numpy as np
a=np.array([1,2,3,4],[5,6,7,8])
print(np.min(a))

#axis 0
print(np.min(a,axis=0))


#Mean,average all the element
b=np.array([1,2,4,5,3])
m=sum(b)/5
#or
print(np.mean(b))

print(np.median(b))
#weights
w=np.array([1,1,1,1,1])
print(np.average(b,weights=w))


#Standard deviation
u=np.mean(b)
myStd=np.sqrt(np.mean(abs(b-u)**2))

#Inbuilt function
dev=np.std(b)

#variance
print(myStd**2)
print(np.var(b))
