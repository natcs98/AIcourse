import cv2
image=cv2.imread("tu.jpg",1)# 1 là chế độ ảnh màu,0 là ảnh xám
px=image[0][0]# truy cập từng điểm ảnh
print(px)
cv2.imshow("image",image)
cv2.waitKey(0)# show ảnh đến khi tắt cửa sổ
cv2.destroyAllWindows()# giải phóng bộ nhớ
