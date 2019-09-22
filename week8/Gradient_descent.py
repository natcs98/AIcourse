import numpy as np

# xử lí data
learning_rate=0.01
X=np.genfromtxt('advertising.csv',delimiter=',',dtype=float,usecols=[0,1,2],skip_header=1)
Y=np.genfromtxt('advertising.csv',delimiter=',',dtype=float,usecols=[3],skip_header=1)
#X = np.random.rand(1000, 1)
#Y = 4 + 3 * X + .2*np.random.randn(1000, 1)
one=np.ones((X.shape[0],1))
X=np.concatenate((one,X),axis=1)
N=X.shape[0]
#khởi tạo w
b=np.dot(X.T,Y)
A=X.T.dot(X)
w=np.dot(np.linalg.pinv(A),b)
print(w)
#Tính đạo hàm
def grad(w):
    return 1/N *X.T.dot(X.dot(w)-Y)
def cost(w):
    return 1/(2*N) *np.sum((Y-X.dot(w))**2)
def grad_descent(w_init,eta):
    w=[w_init]
    for i in range(100):
        w_new=w[-1]-eta*grad(w[-1])
        tmp=np.linalg.norm(w[-1])-np.linalg.norm(w_new)
        if tmp<1e-06:
            break
        w.append(w_new)
    return w[-1],i
print(grad_descent(w,learning_rate))

