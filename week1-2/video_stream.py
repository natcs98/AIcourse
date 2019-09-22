import numpy as np
n=10
m=100
from matplotlib import pyplot as plt

pop=(np.random.random(size=(m,n))-0.5)*100
losses=[]
k1 = np.random.randint(0, m, size=1)
k2 = np.random.randint(0, m, size=1)
    #print(k1," ",k2)
parent_pop=pop.copy()
#print(parent_pop)
s1 = parent_pop[k1].copy()[0]
s2 = parent_pop[k2].copy()
print(parent_pop[k2])
   # print(s1, " ", s2)


