import random
weight=[]
prices=[]
n_generation=1000
max_weight=70
fitness=[]
n=12
m=1000
# load data
def load_data():
    file=open('caitui.csv','r')
    lines=file.readlines()
    global n
    n=len(lines)
    for i in range(len(lines)):
        strings=lines[i].split(',')
        weight.append(float(strings[0]))
        prices.append(float(strings[1]))
    return weight,prices
weight,prices=load_data()
print(weight)
print(prices)
# tao ngau nhien phan tu
def generate_random_value():
    return random.randint(0,1)
# tao individual
def create_individual():
    return [generate_random_value() for i in range(n)]
#tinh fitness
def compute_fitness(individual):
    tien=0
    can=0
    for i in range(len(individual)):
       tien+=individual[i]*prices[i]
       can+=individual[i]*weight[i]
    if can>max_weight:
        tien=tien/1000
    return tien
#selection
def selection(old_population):
    index1=random.randint(0,m-1)
    while True:
        index2=random.randint(0,m-1)
        if index2!=index1:
            break
    if index1> index2:
        return old_population[index1]
    else:
        return old_population[index2]

#crossover
def crossover(individual1,individual2,rate=0.9):
    individual1_new=individual1.copy()
    individual2_new=individual2.copy()
    for i in range(n):
        if random.random()<=rate:
            individual1_new[i]=individual2[i]
            individual2_new[i]=individual1[i]
    return individual1_new,individual2_new
#mutate
def mutate(individual,rate=0.05):
    individual1=individual.copy()
    for i in range(len(individual)):
        if random.random()<=rate:
            individual1[i]=generate_random_value()
    return individual1
# create new population

def create_new(old_population,elitism,gen=1):
    new_population=[]
    sorted_populations=sorted(old_population,key=compute_fitness)
    if gen%1==0:
        fitness.append(compute_fitness(sorted_populations[m-1]))
        print("BEST:",compute_fitness(sorted_populations[m-1]),sorted_populations[m-1])
    while len(new_population)<=m-elitism:
        individual1 = selection(sorted_populations)
        individual2 = selection(sorted_populations)
        # crossover
        individualc1, individualc2 = crossover(individual1, individual2, 0.9)
        # mutate
        individual1 = mutate(individualc1, 0.05)
        individual2 = mutate(individualc2, 0.05)
        new_population.append(individual1)
        new_population.append(individual2)
    for ind in sorted_populations[m - elitism:]:
        new_population.append(ind.copy())
    return new_population
#main
population=[create_individual() for i in range(m)]

for i in range(n_generation):
    population=create_new(population,2,i)
