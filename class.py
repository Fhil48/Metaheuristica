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


def cruza(ch_1, ch_2):
    cut_pto = random.randint(0, len(ch_1))
    return ch_1[:cut_pto] + ch_2[cut_pto:]


def mutation(population):
    n = random.randint(0, len(population))
    population[n]


def ruleta(fitnes, population):
    total = sum(fitnes)
    prop = []
    for i in fitnes:
        prop.append(i/total)
    print(prop)

    n = random.random()
    m = prop[0]
    print(n)
    select = []

    while True:
        for i in range(0, len(prop)-1):
            if n <= m and len(select) < 2:
                select.append(i)
            else:
                m += prop[i+1]
            print(select)

        if (len(select) >= 2):
            if (select[0] == select[1]):
                n = random.random()
                m = prop[0]
            else:
                break
    return select[0], select[1]


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
    # print_table(population[9996])
    # print(fittnes(population[9996]))
    ruleta(fitnes, population)

    n = 1
    while n <= int(arg[6]):
        if int(arg[4]) < random.random()*100:
            i, j = ruleta(fitnes, population)
            cruza(population[i], population[j])
        if int(arg[5]) < random.random()*100:
            mutation(population)
        n += 1
