import cv2
import numpy as np
image=cv2.imread("tu.jpg")
print("shape:",image.shape[0],image.shape[1])
print("size:",image.size)
subimg=image[200:700,200:700]# cắt ảnh
cv2.imshow("image",subimg)
cv2.waitKey(0)