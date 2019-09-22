import numpy as np
from tensorflow.python.ops.metrics_impl import precision


def cau1():
    print(np.arange(0,10))
def cau2():
    arr=np.ones((2,3))>0
    print(arr)
def cau3():
    arr=np.arange(0,10)
    chan=arr[arr%2==0]
    print(chan)
    le=arr[arr%2==1]
    print(le)
def cau4():
    arr=np.arange(0,10)
    arr[arr%2==1]=10
    print(arr)
def cau5():
    arr=np.arange(0,10)
    out=np.where(arr%2==0,11,arr)
    print(out)
def cau6():
    arr=np.arange(0,10)
    arr=arr.reshape(2,-1)
    print(arr)
def cau7():
    arr1=np.arange(0,10).reshape(2,-1)
    arr2=np.arange(10,0,-1).reshape(2,-1)
    out=np.concatenate([arr1,arr2],axis=0)
    print(out)
def cau8():
    arr1 = np.arange(0, 10).reshape(2, -1)
    arr2 = np.arange(10, 0, -1).reshape(2, -1)
    out = np.concatenate([arr1, arr2], axis=1)
    print(out)
def cau9():
    arr=np.arange(1,4)
    out1=np.repeat(arr,2)# lặp lại mỗi phần tử 2 lần
    out2=np.tile(arr,2)# lặp lại tất cả phần từ 2 tần vd 123123
    print(out1)
    print(out2)
def cau10():
    #tim phan tu chung giua 2 mang
    arr1=np.arange(1,6)
    arr2=np.arange(3,9)
    out=np.intersect1d(arr1,arr2)
    print(out)
def cau11():
    # xoa phan tu arr1 cos trong arr2
    arr1 = np.arange(1, 6)
    arr2 = np.arange(3, 9)
    out=np.setdiff1d(arr1,arr2)
    print(out)
def cau12():
    #lay vi tri cac phan tu co gia tri giong nhau va cung vi tri, 2 mang phai cung kich thuoc
    arr1 = np.arange(1, 6)
    arr2 = np.arange(1, 6)
    out=np.where(arr1==arr2)
    print(out)
def cau13():
    #tim tat ca cac phan tu trong pham vi cho truoc
    arr = np.array([1, 7, 3, 9, 4, 8])
    #c1
    out1=np.where((arr>=2)&(arr<=8))
    print(arr[out1])
    #c2
    out2=np.where(np.logical_and(arr>=2,arr<=8))
    print(arr[out2])
    #c3
    out3=arr[(arr>=2)&(arr<=8)]
    print(out3)
def cau14():
    #tao ra mang moi ,tai moi phan tu la max giua 2 mang
    arr1 = np.array([4, 6, 2, 8, 6, 9])
    arr2 = np.array([1, 5, 4, 9, 8, 5])
    out=np.maximum(arr1,arr2)
    print(out)
def cau15():
    arr = np.arange(12).reshape(4, 3)
    print(arr)
    out=arr[:,[1,0,2]]# thay doi thu tu cot 1 0 2
    print(out)
def cau16():
    #thay doi hang
    arr = np.arange(12).reshape(4, 3)
    print(arr)
    out=arr[[1,0,2,3],:]
    print(out)
def cau17():
    #dao nguoc cac dong tu cuoi len dau
    arr = np.arange(12).reshape(4, 3)
    print(arr)
    out = arr[::-1, :]
    print(out)
def cau18():
   #dao nguoc cot
    arr = np.arange(12).reshape(4, 3)
    print(arr)
    out = arr[:, ::-1]
    print(out)
def cau19():
    #tao mang 2x3 random tu o->9 kieu float
    out=np.random.uniform(0,9,[2,3])
    print(out)

