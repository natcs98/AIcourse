import random
def random_search(n=10,m=8):

    res=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            x=random.random()
            if x>0.5:
                res[i][j]=1
    return res
print(random_search(10,8))

