import cv2
import numpy as np
image=cv2.imread("digits.png")
cells=[np.hsplit(row,50) for row in np.vsplit(image,50)]
x=np.array(cells)
cv2.imwrite("so9.png",x[49,49])
