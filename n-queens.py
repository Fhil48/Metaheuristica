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
    print("Padres: ", ch_1, ch_2)
    print("Punto:", cut_pto, ", Hijo:", ch_1[:cut_pto] + ch_2[cut_pto:])
    return ch_1[:cut_pto] + ch_2[cut_pto:]


def mutation(population):
    individuo = population[random.randint(0, len(population)-1)]
    while True:
        n = random.randint(0, len(individuo)-1)
        m = random.randint(0, len(individuo)-1)
        if n != m:
            break
    bubble = individuo[n]
    individuo[n] = individuo[m]
    individuo[m] = bubble


def ruleta(fitnes, population):
    total = sum(fitnes)
    prop = []
    for i in fitnes:
        prop.append(i/total)

    n = random.random()
    m = [prop[0]]
    select = []
    for i in range(1, len(prop)):
        m.append(prop[i]+m[i-1])

    while True:
        n = random.random()
        for i in range(1, len(prop) - 1):
            if  prop[i-1] < n and n <= prop[i] and len(select) < 2:
                select.append(i)
        if len(select) >= 2:
            if select[0] != select[1]:
                break
            else:
                select.pop()
        else: 
            n = random.random()
    return population[select[0]], population[select[1]]


def print_table(individuo):
    n = len(individuo)
    print(individuo, fittnes(individuo))
    for row in range(n):
        print(" ".join("x" if individuo[row] ==
              col else "." for col in range(n)))


if __name__ == "__main__":
    """
    --- input ---
    valor semilla
    tamaño tablero
    tamaño poblacion
    probabilidad de cruza
    probabilidad de mutacion
    numero de iteraciones
    """
    random.seed(arg[1])
    population = generate_population(int(arg[2]), int(arg[3]))
    fitnes = []
    for i in population:
        fitnes.append(fittnes(i))
    ruleta(fitnes, population)

    n = 1
    while n <= int(arg[6]):
        if int(arg[4]) < random.random()*100:
            p_1, p_2 = ruleta(fitnes, population)
            cruza(p_1, p_2)
        if int(arg[5]) < random.random()*100:
            mutation(population)
        n += 1
