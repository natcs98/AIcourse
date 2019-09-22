import numpy as np
import matplotlib.pyplot as plt
#dự đoán giá nhà y=ax+b-> y=t.xbar
#xbar=[1,x] , t=[a,b]
# xử lí data
data=np.genfromtxt('my_house_price_prediction.csv',delimiter=',',dtype=float)
x=data[:,0]
y=data[:,1]
one=np.ones((x.shape[0],1))
xbar=np.c_[(one,x)]
A=xbar.T.dot(xbar)
b=xbar.T.dot(y)
A_1=np.linalg.pinv(A)
w=A_1.dot(b)
print(w)


