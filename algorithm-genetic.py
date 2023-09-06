import numpy as np
import random
from math import ceil, floor
from sys import argv as arg


def generate_population(table_size, population_size):
    n = 0
    population = []
    while n < population_size:
        individuo = list(range(table_size))
        random.shuffle(individuo)
        population.append(individuo)
        n += 1
    return population


def fittnes(individuo):
    colision = 0
    for i in range(len(individuo)):
        for j in range(i+1, len(individuo)):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == j - i:
                colision += 1
    return colision


def cruza(population):
    print("cruza")


def mutation(population):
    print("mutacion")


def ruleta(fitnes, population):
    total = sum(fitnes)
    prop = []
    for i in fitnes:
        prop.append(i/total)
    # for i in prop:
        # print(i)


def print_table(individuo):
    n = len(individuo)
    print(individuo)
    for row in range(n):
        print(" ".join("x" if individuo[row] ==
              col else "." for col in range(n)))


if __name__ == "__main__":
    random.seed(arg[1])
    population = generate_population(int(arg[2]), int(arg[3]))
    fitnes = []
    for i in population:
        fitnes.append(fittnes(i))
    print(population[9996])
    print(fittnes(population[9996]))
    ruleta(fitnes, population)

    """
    n = 1
    while n <= int(arg[6]):
        if int(arg[4]) < random.random()*100:
            cruza(population)
        if int(arg[5]) < random.random()*100:
            mutation(population)
        n += 1
    """
