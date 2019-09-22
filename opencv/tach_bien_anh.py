import numpy as np
import cv2

image=cv2.imread("tachbienjpg.jpg",0)
image2=cv2.Canny(image,0,0)
cv2.imshow("tach bien",image2)
cv2.waitKey(0)
