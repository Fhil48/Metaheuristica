import numpy as np
import random
import time
from math import ceil, floor
from sys import argv as arg, exit


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


def cruza(p_1, p_2):
    cut_pto = random.randint(0, len(p_1)-1)
    ch_1 = p_1[:cut_pto] + p_2[cut_pto:]
    ch_2 = p_1[cut_pto:] + p_2[:cut_pto]
    r1 = []
    r2 = []
    for i in range(len(ch_1)):
        if ch_1.count(i) > 1: 
            r1.append(i)
        if ch_2.count(i) > 1: 
            r2.append(i)
    for i in range(len(r1)):
        bubble = ch_1[ch_1.index(r1[i])]
        ch_1[ch_1.index(r1[i])] = ch_2[ch_2.index(r2[i])]
        ch_2[ch_2.index(r2[i])] = bubble
    return ch_1, ch_2


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
    selection = []
    while len(selection) < 2:
        rand = random.uniform(0, total)
        prop = 0
        for i, fit in enumerate(fitnes):
            prop += fit
            if (prop >= rand):
                selection.append(population[i])
                break
    return selection


def print_table(individuo):
    n = len(individuo)
    print(individuo, fittnes(individuo))
    for row in range(n):
        print(" ".join("x" if individuo[row] ==
            col else "." for col in range(n)))


def parameters():
    if len(arg) < 7:
        print("Los parametros de entrada no son correctos.")
        print("Utilice: n-queens.py <semilla> <tamaño tablero> <tamaño poblacion> <probabilidad de cruza> <probabilidad de mutación> <Iteraciones>")
        exit(1)
    try:
        seed = int(arg[1])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    try:
        board_size = int(arg[2])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    try:
        population_size = int(arg[3])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    try:
        cross_prob = int(arg[4])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    try:
        mutation_prob = int(arg[5])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    try:
        iterations = int(arg[6])
    except ValueError:
        print("Los parametros de entrada no son correctos.")
        exit(1)
    return seed, board_size, population_size, cross_prob, mutation_prob, iterations


def Main():
    tiempo_process_ini = time.process_time()
    seed, board_size, population_size, cross_prob, mutation_prob, iterations = parameters()

    random.seed(seed)
    population = generate_population(board_size, population_size)

    n = 1
    iteracion = -1
    while n <= iterations:
        print(f"iteracion #{n}")
        fitnes = []
        for i in population:
            fitnes.append(fittnes(i))

        if(0 in fitnes):
            iteracion = n
            break
        childrens = []

        while len(population) != len(childrens):
            if cross_prob > random.random()*100:
                p_1, p_2 = ruleta(fitnes, population)
                ch_1, ch_2 = cruza(p_1, p_2)
                childrens.append(ch_1)
                childrens.append(ch_2)
            if mutation_prob > random.random()*100 and len(childrens) > 0:
                mutation(childrens)
        population = childrens
        n += 1
    tiempo_process_fin = time.process_time()
    fitnes = []
    population.sort(key=fittnes)
    
    for i in population:
        fitnes.append(fittnes(i))
    print(fitnes)
    print(f"Tiempo de ejecucion: {tiempo_process_fin-tiempo_process_ini}")
    if(fitnes[0] == 0):
        print(f"iteracion n°: {iteracion} Solucion Factible: {population[0]}")
        print_table(population[0])
    else:
        print(f"Solucion No factible: {population[0]}")



if __name__ == "__main__":

    """
    --- Argumentos ---
    valor semilla
    tamaño tablero
    tamaño poblacion
    probabilidad de cruza
    probabilidad de mutacion
    numero de iteraciones; iteraciones = generaciones, una generacion es crear tp hijos para reemplazar la poblacion actual
    """
    Main()

    """
    Agregar readme de instalacion y caso de uso donde el programa si encontro una solucion.
    """

    # python n-quens.py 10 16 800 90 20 1000