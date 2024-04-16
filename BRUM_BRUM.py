import math
import random

all_cities = [[16.47, 96.10], [16.47, 94.44], [22.39, 93.37], [25.23, 97.24], [22.00, 96.05], [20.47, 97.02],
              [17.20, 96.29], [20.09, 92.52], [16.30, 97.38], [14.05, 98.12], [16.53, 97.38], [21.52, 95.59],
              [19.41, 97.13], [20.09, 94.54]]


def distance_cal(city1, city2):
    x_diff = city1[0] - city2[0]
    y_diff = city1[1] - city2[1]
    return math.sqrt(x_diff ** 2 + y_diff ** 2)


fittest = float('inf')
fittest_path = []
fittest_offspring = float('inf')
final_best_path = []

for _ in range(10):
    for _ in range(100):
        individual = all_cities.copy()
        random.shuffle(individual)

        for _ in range(8):
            r = random.randint(0, 13)
            r2 = random.randint(0, 13)
            individual[r], individual[r2] = individual[r2], individual[r]

        fitness = sum(distance_cal(individual[i], individual[i + 1]) for i in range(13))

        if fitness < fittest:
            fittest = fitness
            fittest_path = individual.copy()

    for _ in range(2):
        rm = random.randint(0, 13)
        rm2 = random.randint(0, 13)
        fittest_path[rm], fittest_path[rm2] = fittest_path[rm2], fittest_path[rm]

    offspring_fitness = sum(distance_cal(fittest_path[i], fittest_path[i + 1]) for i in range(13))
    if offspring_fitness < fittest_offspring:
        fittest_offspring = offspring_fitness
        final_best_path = fittest_path.copy()

print('BEST POSIBLE ROUTE is:')
print(final_best_path)
print('THE FITNESS OF SELECTED ROUTE IS:')
print(fittest_offspring)
