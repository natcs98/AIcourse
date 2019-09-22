import numpy as np
from numpy import nan

def cau1():
    #Thay thế tất cả các phần tử trong một mảng có giá trị lớn hơn 30 thành 30 và dưới 10 thành 10.
    #input: [28. 15. 22. 42.  1.  7. 34. 41.  8. 29.]
    #output: [28. 15. 22. 30. 10. 10. 30. 30. 10. 29.]
    x=np.array([28., 15., 22., 42.,  1.,  7., 34., 41.,  8., 29.])
    out=np.where(x<10 ,10,x)
    out=np.where(out>30,30,out)
    print(out)
#cau1()
def cau2():
    #Lấy vị trí của 3 giá trị lớn nhất trong một mảng numpy
    #input: [28. 15. 22. 42.  1.  7. 34. 41.  8. 29.]
    #output: [6 7 3]
    data=np.array([28. ,15. ,22. ,42.  ,1.  ,7. ,34. ,41. , 8. ,29.])
    res=np.argsort(data)
    print(res[-3:])
#cau2()
def cau3():
    #input: [array([0, 1, 2]) array([3, 4, 5, 6]) array([7, 8, 9])]
    #output: [0 1 2 3 4 5 6 7 8 9]
    x=np.array([0, 1, 2])
    y=np.array([3, 4, 5, 6])
    z=np.array([7, 8, 9])
    #c1
    out=np.concatenate([x,y,z],axis=0)
    print(out)
    #c2
    out1=np.hstack([x,y,z])
    print(out1)
    #c3
    out2=np.r_[x,y,z]
    print(out2)

#cau3()
def cau4():
    #Tạo one-hot encoding cho một mảng numpy.
# One-hot encoding nhằm chuyển đổi mỗi giá trị (số nguyên) n
# thành một vector v mà vị trí thứ n trong vector v mang giá trị 1 và
# tất cả vị trí khác đều mang giá trị 0.
#[2 1 3 3 1 2]
#output: array([[0., 1., 0.],
              #[1., 0., 0.],
              #[0., 0., 1.],
              #[0., 0., 1.],
              #[1., 0., 0.],
              #[0., 1., 0.]])
    input=np.array([2 ,1 ,3 ,3 ,1 ,2])
    x=input.max()
    y=input.size
    res=np.zeros((y,x),dtype=float)
    for i in range(y):
        res[i,input[i]-1]=1
    print(res)
#cau4()
def cau5():
    #   Sắp xếp các phần tử trong một mảng 1 chiều
#
#  input: [3 6 4 8]
# output: [3 4 6 8]
    x=np.array([3,6,4,8])
    x.sort()
    print(x)
#cau5()
def cau6():
    #Tìm giá trị lớn nhất trong mỗi hàng và mỗi cột của một mảng 2d
#input
#[[5 1 7]
 #[3 5 2]
 #[6 4 5]]
#output
#Max by column
#[6 5 7]
#Max by row
#[7 5 6]
    x=np.array([[5,1 ,7],
                [3, 5, 2],
                [6, 4, 5]])
    col=x.max(axis=0)
    row=x.max(axis=1)
    print(col)
    print(row)
#cau6()
def cau7():
    #Tìm các phần tử trùng lặp (lần xuất hiện thứ 2 trở đi) trong mảng đã cho
#và đánh dấu chúng là True. Lần đầu tiên xuất hiện là False.

#[0 3 3 1 2 0 2 0]
#[False False  True False False  True  True  True]
    x=np.array([0 ,3, 3, 1, 2, 2 ])
    res=np.ones(x.shape[0],dtype=bool)
    z=np.unique(x)#0 1 2 3
    for i in range(x.shape[0]):
        if x[i] in z:
            index=np.argwhere(x[i]==z)
            res[i]=False
            z=np.delete(z,index)
    print(res)

cau7()
def cau8():
    #Trừ theo dòng mảng 2 chiều arr2d bằng mảng 1 chiều arr1d
    arr2d = np.array([
        [3, 3, 3],
        [4, 4, 4],
        [5, 5, 5]
    ])

    arr1d = np.array([1, 1, 1])
    res=arr2d-arr1d
    print(res)
#cau8()
def cau9():
    #Bỏ tất cả các giá trị nan từ một mảng numpy
    x=np.array([1.,  2.,  3.,nan,  5.,  6.,  7., nan])

    index=np.where(np.isnan(x))
    x=np.delete(x,index)
    print(x)
#cau9()
def cau10():
    #Lấy tất cả vị trí nơi các phần tử có giá trị khác nhau
# input
# arr1: [3 4 5 6 7 8]
# arr2: [3 3 6 6 7 7]
# output
# [1, 2, 5]
    arr1=np.array([3,4,5,6,7,8])
    arr2=np.array([3,3,6,6,7,7])
    index=np.where(arr1!=arr2)[0]
    print(index)
#cau10()