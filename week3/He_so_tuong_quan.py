import  numpy as np
from PIL import Image
import math
img1=Image.open('img1.png')
img2=Image.open(('img2.png'))
i1=np.asarray(img1).flatten().tolist()# chuyển image về mảng 2 chiều xong chuyển về mảng numpy 1 chiều chuyển về list
i2=np.asarray(img2).flatten().tolist()
def ham(x,y):
    n=len(x)
    tongx=sum(x)
    tongy=sum(y)
    tongxy=0
    xy=[]
    x2=[]
    y2=[]
    for i in range(0,n):
        xy.append(x[i]*y[i])
        x2.append(x[i]**2)
        y2.append(y[i]**2)
    tongxy=sum(xy)
    tongx2=sum(x2)
    tongy2=sum(y2)
    res=(n*tongxy-tongx*tongy)/(math.sqrt((n*tongx2-tongx**2)*(n*tongy2-tongy**2)))
    return res
print(ham(i1,i2))
