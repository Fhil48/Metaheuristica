import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def InitializeEcosystem(n, c, items):
    
    x = np.zeros(n, dtype=int)
    for i in range(n):
        x[i] = np.random.randint(0,2)
    best_value = EvaluateEcosystem(x,items)
    if(np.sum(x*np.array(items)[:,2]) > c):
        x = np.zeros(n, dtype=int)
        best_value = -1
    return x, best_value

def Probabilities(n, Tau):
    p = np.zeros(n)
    for i in range(1, n+1):
        p[i-1] = round(i**(-Tau),2)
    proportion = np.array(p/sum(p))
    return proportion

def Roulette(n, probabilities):
    return np.random.choice(n, p=probabilities)

def Replacement(solution, probabilities, items, c):
    x = solution.copy()
    x_j = Roulette(len(x), probabilities)
    x[x_j] = 1 - x[x_j]
    while np.sum(x * items[:, 2]) > c:
        objetos_incluidos = np.where(x == 1)[0]

        if len(objetos_incluidos) == 0:
            break
        
        objeto_a_quitar = objetos_incluidos[np.argmin(items[objetos_incluidos, 1])]

        x[objeto_a_quitar] = 0
    return x

def Fitness(n, items, solution):
    fitness = []
    for i in range(n):
        fitness.append(solution[i]*items[i][2])
    return fitness

def EvaluateEcosystem(backpack, items):
    return np.sum(backpack*np.array(items)[:,1])

def DataBackpack(file_path):
    backpack = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if(lines[i].split() == []):
                continue
            if lines[i].strip().startswith('knapPI'):
                case = lines[i].strip()
                items = []
            elif(lines[i].split()[0] == 'n'):
                N = int(lines[i].split()[1])
            elif(lines[i].split()[0] == 'c'):
                C = int(lines[i].split()[1])
            elif(lines[i].split()[0] == 'z'):
                Z = int(lines[i].split()[1])
            elif(lines[i].split()[0] == 'time'):
                time = float(lines[i].split()[1])
            elif(lines[i].split()[0] != '-----'):
                items.append(list(map(int,lines[i].strip().split(','))))
            else:
                backpack.append({
                    'Backpack': case,
                    'N': N,
                    'C': C,
                    'Z': Z,
                    'Items': items
                })
    return backpack


def main():
    # archivo_csv_small = 'input/small/knapPI_9_50_1000.csv'
    # archivo_csv_hard = 'input/hard/knapPI_16_20_1000.csv'
    archivo_csv_large = 'input/large/knapPI_9_50_100000.csv'
    Tau = [0.6,0.8,1,1.2,1.4,1.6,1.8,2.0, 2.2, 2.4]
    iterations = 1000
    seed = 30
    data = DataBackpack(archivo_csv_large)
    d = data[94]
    results = {}
    for s in range(seed):
        np.random.seed(s)
        for t in Tau:

            # for d in data:
            x_best_solution, x_best_value_solution = InitializeEcosystem(d['N'], d['C'], d['Items'])
            for i in range(iterations):
                probabilities = Probabilities(d['N'], t)
                fitness = Fitness(d['N'],d['Items'],x_best_solution)
                rank_fitness = np.argsort(fitness)[::-1]
                d['Items'] = np.array(d['Items'])[rank_fitness]
                x_best_solution = x_best_solution[rank_fitness]

                x_solution = Replacement(x_best_solution, probabilities, d['Items'], d['C'])
                x_value_solution = EvaluateEcosystem(x_solution, d['Items'])
                # print(' valor: ', x_value_solution, 'peso: ',np.sum(x_solution*np.array(d['Items'])[:,2]) ,  np.sum(x_solution*np.array(d['Items'])[:,2]) <= d['C'])
                if(np.sum(x_solution*np.array(d['Items'])[:,2]) <= d['C'] and x_value_solution > x_best_value_solution):
                    x_best_solution = x_solution
                    x_best_value_solution = x_value_solution
                if(x_best_value_solution == d['Z']):
                    break

            results.setdefault(t, []).append(x_best_value_solution)
                
            print('solucion para: ', d['Backpack'], ', valor para Tau: ', t, ', valor semilla: ', s, ' nueva solucion final: ', x_best_solution, ' valor final: ', x_best_value_solution, ' valor optimo: ', d['Z'])

    df = pd.Series(results[Tau[0]], name=str(Tau[0])).to_frame()
    for t in Tau[1:]:
        arr = results[t]
        df = df.join(pd.Series(arr, name=str(t)))

    
    sns.boxplot(df)
    plt.suptitle('Tau vs Z - ' + d['Backpack'])
    plt.xlabel("Tau")
    plt.ylabel("Z")
    plt.show()
   
if __name__ == "__main__":
    main() 