import numpy as np
#to create the list
a=np.array([1,2,3,4,5,6])

print(a)

#print the dimension of the array
print(a.shape)


#2d array
c=np.array([1,2,3],[4,5,6])
print(c)

#create zero,Ones Custom array
a=np.zeros((3,3))
print(a)

b=np.ones((2,3))


#array of some constant
c=np.full((3,2),5)
print(c)

#Indentiy Matrix -Size/Square matrix
d=np.eye(4)
print(d)

#Random Matrix
randomMatrix=np.random.random((2,3))
print(randomMatrix)

print(randomMatrix[:,2])


#Mathematical Operations
x=np.array([1,2],[3,4])
y=np.array([5,6],[7,8])
print(x+y)
#or
print(np.add(x,y))

#Matrix Multiplication /Dot Product==>Scalar value
print(np.dot(x,y))

a=np.array([1,2,3,4])
b=np.array([1,2,3,4])

print(a.dot(b))

#gave sum of whole array
print(sum(a))
print(np.sum(a))


#stacking of array
print(a)
b=b**2
print(b)

np.stack((a,b),axis=0)

print(a)
a=a.reshape((4,2))
print(a)