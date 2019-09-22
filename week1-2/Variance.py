data=[7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
def Mean_fun(number):
    n=len(number)
    s=sum(number)
    return s/n
def Variance_fun(number):
    m=Mean_fun(number)
    daff=[]
    for i in number:
        daff.append((i - m) ** 2)

    return Mean_fun(daff)
print(Mean_fun(data))
