import cv2

ima=cv2.imread("tu.jpg")
cv2.line(ima,(0,0),(720,720),(0,0,25),5)
cv2.imwrite("line_tu.jpg",ima)