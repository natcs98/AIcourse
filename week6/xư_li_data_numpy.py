import numpy as np
import numpy.core.defchararray as np_f
# lấy các đặc trưng và lưu vào biến X
X = np.genfromtxt('Iris.csv', delimiter=',', dtype='float', usecols=[1,2,3,4], skip_header=1)
print(X.shape)
# lấy species và lưu vào biến y
y = np.genfromtxt('Iris.csv', delimiter=',', dtype='str', usecols=5, skip_header=1)
# thay chuỗi bằng số
categories = np.unique(y)
for i in range(categories.size):
    y = np_f.replace(y, categories[i],str(i))# tim các vị trí trong y mà y=categories[i] rồi thay thế bằng kí tự 'i'
# đưa về kiểu float
y = y.astype('float')
print(y)