import numpy as np
import  matplotlib.pyplot as plt
X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
              2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])
rate=0.01
# xử lí data đầu vào
one=np.ones((1,X.shape[1]))
X=np.concatenate((one,X),axis=0)
w_init=np.random.rand(X.shape[0],1)
print(X.shape[0])
def sigmoid(s):
    return 1/(1+np.exp(-s))
def Logistic_regression(X,y,w_init,rate,tol = 1e-4,max_count=1000):
    w=[w_init]
    d=X.shape[0]
    N = X.shape[1]

    count=0
    check_w_after=20
    while count<max_count:
        mix_id = np.random.permutation(N)# 1 dãy từ 0-n nhưng trật tự thay đổi hỗn loạn
        count += 1
        for i in mix_id:
            xi=X[:,i].reshape(d,1)
            yi=y[i]
            si=np.dot(w[-1].T,xi)
            zi=sigmoid(si)
            w_new=w[-1]+rate*(yi-zi)*xi



            w.append(w_new)
    return w
w=Logistic_regression(X,y,w_init,0.01)
s1=w[-1].T.dot(X)
z1=sigmoid(s1)
print(z1)



