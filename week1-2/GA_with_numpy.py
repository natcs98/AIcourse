import numpy as np
from matplotlib import pyplot as plt
n_generation=100
n=10
m=100
CROSS_RATE=0.9
MUTATE_RATE=0.05
BOUND=100
def sphere_funtion(x):
    return np.sum(x*x,axis=1) #x=(-50,50) tinh tong theo chieu axis=1-chieu ngang
def compute_fitness(pred):
    return 1/(pred+1)
def selection(pop,fitness):
    idx=np.random.choice(np.arange(m),size=m,replace=True,p=fitness/fitness.sum())
    #idx là 1 mảng num py không phải 1 sô
    print(idx)
    return pop[idx] #-> pop[idx] là [[]] là 1 mảng 2 chiều chứ không phải 1 hàng

def crossover(s1,s2):
    prop=np.random.rand(n)
    addition=prop<CROSS_RATE
    tmp =s1[addition]
    s1[addition]=s2[addition]
    s2[addition]=tmp
    return s1,s2
def mutate(x):
    tmp=(np.random.rand((n))-0.5)*100
    prop=np.random.rand(n)
    addition=prop<MUTATE_RATE
    x[addition]=tmp[addition]
    return x


pop=(np.random.random(size=(m,n))-0.5)*100
losses=[]
for g in range(n_generation):
    cost_value=sphere_funtion(pop) # mảng np giá trị của hàm sphere
    fitness=compute_fitness(cost_value) #mảng fitness
    if g%1==0:
        #print("cost:" ,np.min(cost_value))
        losses.append(np.min(cost_value))
        #print(pop[np.argmax(fitness)])
    pop=selection(pop,fitness)


    parent_pop=pop.copy()
    for i in range(m//2-2):
        k1=np.random.randint(0,m,size=1)
        k2=np.random.randint(0,m,size=1)
        #vì k1 và k2 là 1 mảng numpy có 1 hàng và 1 cột
        #s1=parent_pop[k1].copy() tạo ra s1 là 1 mảng 2 chiều có 1 hàng
        #s1=parent_pop[k1].copy()[0] tạo ra s1 là 1 mảng 1 chiều
        s1=parent_pop[k1].copy()[0]
        s2=parent_pop[k2].copy()[0]
        s1,s2=crossover(s1,s2)
        s1=mutate(s1)
        s2=mutate(s2)
        pop[i*2][:]=s1
        pop[i*2+1][:]=s2
    two_best=fitness.argsort()[-2:]
    pop[m-2][:]=parent_pop[two_best[0]].copy()[0]
    pop[m - 1][:] = parent_pop[two_best[1]].copy()[1]
plt.plot(losses[:100])
plt.show()
