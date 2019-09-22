import numpy as np
import matplotlib.pyplot as plt
np.random.seed(11)
N=500
mean=[[2,2],[3,8],[9,2]]
cov=[[1,0],[0,1]]
X0=np.random.multivariate_normal(mean[0],cov,size=N)
X1=np.random.multivariate_normal(mean[1],cov,size=N)
X2=np.random.multivariate_normal(mean[2],cov,size=N)
X=np.concatenate((X0,X1,X2),axis=0)
k=3
original_label=np.asarray([0]*N+[1]*N+[2]*N)

def kmean_display(X,label):
    X0=X[label==0,:]
    X1=X[label==1,:]
    X2=X[label==2,:]
    plt.title("kmean cluster")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(X0[:,0],X0[:,1],'b^',markersize=4,alpha=.8)# b^ blue tam giác,markersize :độ to của điểm
    plt.plot(X1[:, 0], X1[:, 1], 'go',markersize=4,alpha=.8)# go là green hình tròn
    plt.plot(X2[:, 0], X2[:, 1], 'rs',markersize=4,alpha=.8)# rs là red square
    plt.show()
kmean_display(X,original_label)
