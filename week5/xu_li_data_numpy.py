from builtins import print

import numpy as np

def cau1():
    # doc dữ liệu từ data xử dụng hàm genfromtxt,dữ liệu trả về mảng 2 chiều
    iris=np.genfromtxt('iris.csv',delimiter=',',dtype=object)
    print(iris.shape)
    print(iris)
#cau1()
def cau2():
    #đọc giống câu 1 nhung dtype=none.dữ liệu trả về mảng 1 chiều,các phần tử là kiểu tuple
    iris = np.genfromtxt('iris.csv', delimiter=',', dtype=None)
    print(iris.shape)
    print(iris)
#cau2()
def cau3():
    #mảng 2 chiều gồm 4 cột đầu tiên
    #c1
    iris = np.genfromtxt('iris.csv', delimiter=',', dtype=None)
    out1=np.array(row.tolist()[:4] for row in iris)
    print(out1)
    #c2
    iris2=np.genfromtxt('iris.csv', delimiter=',', dtype=None,usecols=[0,1,2,3])#usecols=usecolums
    print(iris2)
#cau3()
#Tìm giá trị trung bình (mean), trung vị (median), độ lệch chuẩn (standard deviation) của cột sepal_length của tập dữ liệu iris (cột thứ 1).
#Mean  (trung bình) được tính bằng tổng của tất cả các giá trị trong mảng và chia cho kích thước mảng.
#Số trung vị (Median) là giá trị giữa trong một phân bố
#Độ lệch chuẩn (Standard deviation) : Độ lệch chuẩn mô tả sự phân tán của dữ liệu.
def cau4():
    out1=np.genfromtxt('iris.csv',delimiter=',',dtype=float,usecols=[0])
    mean,median,standard=out1.mean(),np.median(out1),np.std(out1)
    print(mean,median,standard)
#cau4()
def cau5():
    #Chuẩn hóa (normalize) cột sepallength để giá trị nằm trong khoảng từ 0 đến 1.
    #cong thức a-a.min/a.max-a.min hoặc a-a.min/a.ptp  a.ptp là hàm lấy phạm vi dữ liệu
    out1 = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0])
    res=(out1-out1.min())/(out1.max()-out1.min())
    print(res)
#cau5()
def cau6():
    # tính hàm sofmax cho côt 1
    #công thức 1 res= exp(z)/sum(exp(z)

    out=np.genfromtxt('iris.csv',delimiter=',',dtype='float',usecols=[0])
    res=np.exp(out)/np.sum(np.exp(out))
    np.set_printoptions(precision=4)
    print(res)
    #công thức 2 res=exp(z-b)/sum(exp(z-b) với b=max(z)
    ex=np.exp((out-out.max()))
    re=ex/np.sum(ex)
    print(re)
#cau6()
def cau7():
    #Đọc tập dữ liệu Iris dùng hàm np.genfromtxt() với dtype='float'. Dữ liệu trả về là một mảng 2 chiều,
    # với các phần tử có kiểu là float cho số và nan (không xác định) cho chuỗi.
    # Tìm vị trí có giá trị không xác định trong mảng numpy
    out=np.genfromtxt('iris.csv',delimiter=',',dtype='float')
    print(out[:5])
    print(np.isnan(out).sum()) #tinh so phan tu nan
    res=np.where(np.isnan(out))
    print(res)
#cau7()
def cau8():
    # Đọc 4 cột dữ liệu đầu tiên, và lọc các dòng có petallength (cột thứ 3) > 1.5 và sepallength (cột thứ 1) < 5.0.
    out=np.genfromtxt('iris.csv',delimiter=',',dtype=float,usecols=[0,1,2,3])
    add=(out[:,2]>1.5 )& (out[:,0]<5.0)
    print(out[add])
#cau8()
def cau9():
    #tim moi tuong quan giua cot 1 va cot 3
    out=np.genfromtxt('iris.csv',delimiter=',',dtype='float',usecols=[0,1,2,3])
    #dung ham corrcoef cua np (correlation coefficient )
    res=np.corrcoef(out[:,0],out[:,2])
    print(res)
#cau9()
def cau10():
    #tim phan tu duy nhat trong mang cot 4
    out=np.genfromtxt('iris.csv',delimiter=',',dtype=object)
    res=np.unique(out[:,4])
    print(res)
#cau10()
def cau11():
    #Chuyển đổi cột 3 petallength thành mảng như sau
#Nhỏ hơn 3   –>   ‘small’
#Từ 3->5        –>   ‘medium’
#Lớn hơn 5   –>   ‘large’
    out = np.genfromtxt('iris.csv', delimiter=',', dtype=object)
   # print(out)
    bin=np.digitize(out[:,1].astype(float),[0,3,5,10])#tạo ra các biến trong các khoảng 1:0->3,2:3->5,3:5->10
    #print(bin)
    lablel={1:'small',2:'medium',3:'lagre'}
    print(type(lablel))
    res=[lablel[x] for x in bin]
   # print(res)
cau11()