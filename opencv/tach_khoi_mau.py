import numpy as np
import cv2

blue=np.uint8([[[232,162,0]]])#màu xanh trong hệ màu rgb// r=0,g=162,b=232
hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)# chuyển sang hệ hsv// convert to color
print(hsv_blue)
image=cv2.imread("anhkhoimau.png",1)
image1=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)# đổi sang hệ mau hsv
minMau=np.array([97,255,232])
maxMau=np.array([100,255,232])
mask=cv2.inRange(image1,minMau,maxMau)# tạo mặt lạ lọc màu trong khoảng min -> max tạo ra 1 ảnh đen trắng
final=cv2.bitwise_and(image,image,mask=mask)#lọc image qua mask,bằng cách and bit
cv2.imshow("anh mau",final)
cv2.waitKey(0)