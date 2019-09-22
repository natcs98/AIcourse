import numpy as np
import cv2
# tao mang từ 1 list
l=[1,2,3,4,5,6,7,8,9,10]
a=np.array(l)
print(a)
#thay doi shape
a=a.reshape((2,5))
print(a)
#tạo mảng toàn 0 và toàn 1
mot=np.ones((4,5))
khong=np.zeros(5)
print(mot)
print(khong)
#mảng full 1 phần tử
full=np.full((2,3),9)
print(full)
#ma trận đường chéo chính toàn 1
cheo=np.eye(4)
print(cheo)
#mang ngẫu nhiên
r=np.random.randint(0,2,(4,5))
print(r)
#mảng numpy điều kiện
con=np.where(a<5,a,0)# tường đương if a<5 đúng thì chọn a sai thì chọn 0
print(con)
#chuyển mảng 2 chiều về mảng 1 chiều
mot_chieu=con.flatten()
print(mot_chieu)
#ma trận đường chéo từ 1 -> n
vd=np.arange(1,6)
cheon=np.random.random(size=(5,5))
print(cheon)
#sicling
sclin=con[0:2,0:3]
print(sclin)
#mang true false
bo_index=(con>0)
print(bo_index)
print(con[bo_index])
a=a.flatten()
b=[]
b=a.copy().tolist()
b.reverse()
print(np.sum(cheon))
#print(cheon)
k1 = np.random.randint(0, 4, size=1)
c=cheon[4].copy()
print(c)
