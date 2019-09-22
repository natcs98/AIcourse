import numpy as np

#xu li data
x=np.genfromtxt('advertising.csv',delimiter=',',dtype=float,usecols=[0,1,2],skip_header=1);
y=np.genfromtxt('advertising.csv',delimiter=',',dtype=float,usecols=3,skip_header=1);
one=np.ones((x.shape[0],1))
xbar=np.concatenate((one,x),axis=1)
print(xbar)
A=np.dot(xbar.T,xbar)
b=np.dot(xbar.T,y)
w=np.dot(np.linalg.pinv(A),b)
np.printoptions(percision=10)
tmp=np.array([1,100,10,10000])
print(w)
print(w*tmp)
