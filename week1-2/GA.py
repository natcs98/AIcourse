import random
from collections import Counter
n=20
m=10
fitness=[]
# khoi tao mang populations
def generate_random_value():
    return random.randint(0,1)

def create_individual():
    return [generate_random_value() for i in range(n)]
populations=[create_individual() for i in range(m)]
#tinh fitness
def compute_fitness(individual):
    return sum(gen for gen in individual)
#sắp xếp population theo fitness từ nhỏ đến lớn
# selection random cap so

def selection(old_populations):
    index1=random.randint(0,m-1)
    while True:
        index2=random.randint(0,m-1)
        if index2!=index1:
            break
    if(index1>index2):
        return old_populations[index1]
    else:
        return old_populations[index2]
# crossover lai ghép
def crossover(individual1,individual2,rate=0.9):
    individual1_new=individual1.copy()
    individual2_new=individual2.copy()
    for i in range(n):
        if random.random()<=0.9:
            individual1_new[i]=individual2[i]
            individual2_new[i]=individual1[i]
    return individual1_new,individual2_new
#mutate đột biến
def mutate(individual, rate=0.05):
    for i in range(n):
        if random.random()<=0.05:
            individual[i]=generate_random_value()
    return individual
#main
def create_new(old_populations,elitism,gen):
    new_population=[]
    sorted_populations=sorted(old_populations,key=compute_fitness)
    if gen%1==0:
        fitness.append(compute_fitness(sorted_populations[m-1]))
        print("BEST:",compute_fitness(sorted_populations[m-1]))
    while len(new_population)<m-elitism:
        # selection
        individual1=selection(sorted_populations)
        individual2=selection(sorted_populations)
        # crossover
        individualc1,individualc2=crossover(individual1,individual2,0.9)
        #mutate
        individual1=mutate(individualc1,0.09)
        individual2=mutate(individualc2,0.09)
        new_population.append(individual1)
        new_population.append(individual2)
    for ind in sorted_populations[m-elitism:]:
        new_population.append(ind.copy())
    return  new_population
for i in range(40):
    populations=create_new(populations,2,i)








