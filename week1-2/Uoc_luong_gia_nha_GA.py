import random
n=2
m=100
n_generation=10000
loss=[]
#load data
def load_data():
    file=open('data.csv','r')
    lines=file.readlines()
    areas=[]
    prices=[]
    for i in range(len(lines)):
        string =lines[i].split(',')
        areas.append(float(string[0]))
        prices.append(float(string[1]))
    file.close()
    return areas,prices
areas,prices=load_data()
#random value
def  generate_random_value(bound=5):
    return (random.random())*bound

# tao tung ca the
def create_individual():
    return [generate_random_value() for i in range(n)]


#tinh loss
def compute_loss(individual):
    a=float(individual[0])
    b=float(individual[1])
    estimate_price=[a*x+b for x in areas]
    estimate_price=[abs(x) for x in estimate_price]
    losses=[abs(est_y-gty) for est_y,gty in zip(estimate_price,prices) ]
    return sum(losses)

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
        loss.append(compute_loss(sorted_populations[m-1]))
        print("BEST:",compute_loss(sorted_populations[m-1]),sorted_populations[m-1])
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

