import numpy as np
import random
# from math import ceil, floor
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
    print(individuo)
    colision = 0
    for i in range(len(individuo)):
        print("colision: ", colision)
        for j in range(i+1, len(individuo)):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == j - i:
                colision += 1
    return colision


def cruza(ch_1, ch_2):
    cut_pto = random.randint(0, len(ch_1)-1)
    # print("Padres: ", ch_1, ch_2)
    # print("Punto:", cut_pto, ", Hijo:", ch_1[:cut_pto] + ch_2[cut_pto:])
    return ch_1[:cut_pto] + ch_2[cut_pto:], ch_1[cut_pto:] + ch_2[:cut_pto]
    #Falta correccion que verifique que los hijos no tengan valroes repetidos. random de faltantes[0] a faltantes[n] quitar seleccionado y continuar hasta que faltantes sea 0.
    #comprobar con los repetidos del segundo hijo al azar e intercambiar entre repetidos en los hijos


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
        m.append(m[i-1]+prop[i])
    while True:
        n = random.random()
        for i in range(1, len(prop) - 1):
            if  m[i-1] < n and n <= m[i] and len(select) < 2:
                print("prop", m[i-1], ", ", m[i], ": ",n)
                select.append(i)
                print(select)
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
              col else "⋅" for col in range(n)))

def main():
    random.seed(arg[1])
    population = generate_population(int(arg[2]), int(arg[3]))
    childrens = []
    fitnes = []


    n = 1
    while n <= int(arg[6]):
        print(population)
        for i in population:
            print(fittnes(i))
            fitnes.append(fittnes(i))
        print("fitnes: ", fitnes)
        print(f"Generacion: {n}, tamaño generacion: {len(population)}, generacion: {fitnes}")
        while len(population) != len(childrens):
            if int(arg[4]) < random.random()*100:
                p_1, p_2 = ruleta(fitnes, population)
                ch_1, ch_2 = cruza(p_1, p_2)
                childrens.append(ch_1)
                childrens.append(ch_2)
                if int(arg[5]) < random.random()*100:
                    mutation(childrens)
        n += 1
        
        population = childrens
        childrens = []
        fitnes = []

    population.sort(key=fittnes)
    print(population)
    print_table(population[0])

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
    main()

    """
    poblacion = nueva poblacion hijo, aplicar mutacion al hijo generado, 
    De una cruza deben salir dos hijos.
    """