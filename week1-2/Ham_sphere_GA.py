import random
#ham sphere f(x)=x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
#tim min của hàm sphere x=(-20;20)
n=6
m=50
n_generation=100
fitness=[]

#tao random cho tung gen
def  generate_random_value(bound=20):
    return (random.random()*2-1)*bound

# tao tung ca the
def create_individual():
    return [generate_random_value() for i in range(n)]


#tinh loss
def compute_loss(individual):
    return sum(gen*gen for gen in individual)

#tinh fitness
def compute_fitness(individual):
    return 1/(compute_loss(individual)+1)

#crossover
def crossover(individual1,individual2,rate=0.9):
    individual1_new=individual1.copy()
    individual2_new=individual2.copy()
    for i in range(n):
        if random.random()<=0.9:
            individual1_new[i]=individual2[i]
            individual2_new[i]=individual1[i]
    return individual1_new,individual2_new

#mutate
def mutate(individual, rate=0.05):
    for i in range(n):
        if random.random()<=0.05:
            individual[i]=generate_random_value()
    return individual

#selection
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

#creat population
def create_new(old_populations,elitism,gen):
    new_population=[]
    sorted_populations=sorted(old_populations,key=compute_fitness)
    if gen%1==0:
        fitness.append(compute_loss(sorted_populations[m-1]))
        print("BEST:",compute_loss(sorted_populations[m-1]))
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

#main
populations=[create_individual() for i in range(m)]
for i in range(n_generation):
    populations=create_new(populations,2,i)