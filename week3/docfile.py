import os
file=open('Iris.csv ','r')
lines=file.readlines()
data=[]
Min=[]
Mean=[]
Max=[]
def min_fun(data,i):
    res=data[0][i]
    for j in range(0,len(data)):
         res=min(res,data[j][i])
    return res
def max_fun(data,i):
    res = data[0][i]
    for j in range(0, len(data)):
        res = max(res, data[j][i])
    return res
def mean_fun(data,i):
    res=0;
    n=len(data)
    for j in range(0,n):
        res+=data[j][i]
    return res/n
def dem_mau(data,mau):
    res=0
    for i in range(0,len(data)):
        if data[i][4]==mau:
            res+=1
    return res
for i in range (1,len(lines)):
    string=lines[i].split(',')
    sepal_Length = float(string[1].strip())
    sepal_Width = float(string[2].strip())
    petal_Length = float(string[3].strip())
    petal_Width = float(string[4].strip())
    species = 0
    if string[5].strip()=='Iris-versicolor' :
        species=1
    elif string[5].strip()=='Iris-virginica':
        species=2
    data.append([sepal_Length,sepal_Width,petal_Length,petal_Width,species])
  #  print('%s;%s;%s;%s;%s;%s'%(string[0],string[1],string[2],string[3],string[4],string[5]))
Min.append(min_fun(data,0))

print(Min[0])

file.close()