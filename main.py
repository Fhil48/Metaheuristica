import numpy as np
import pandas as pd
import sys
import time

file_path = './input/knapPI_9_50_1000.csv'
archivo = pd.read_csv(file_path, skiprows=5, header=None, nrows=50)
peso = archivo[2].values
valor = archivo[1].values
# print(len(archivo))
# print("pesos: ", peso)
# print("valores: ",valor)
def Parametros():
    # entrada = sys.argv[1]
    # semilla = sys.argv[2]
    # i = sys.argv[3]
    # T = sys.argv[4]
    #entrada = sys.argv[1]
    
    semilla = 1
    file = pd.read_csv(file_path, header=None, skiprows=1, nrows=2, delim_whitespace=True)
    i = 1000
    c = file.iloc[1, 1]    
    T = 1.5
    return file_path, semilla, i, T, c

def EvaluarEcosistema(X):
    selected_indices = np.where(X == 1)[0]
    total_cost = np.sum(valor[selected_indices])
    total_weight = np.sum(peso[selected_indices])

    return total_cost, total_weight

def Reemplazo():
    pass

def Ruleta(proporcion):
    rd = np.random.random(1)
    aux = 0
    for i in range(0,len(proporcion)-1):
        if(aux + proporcion[i] > rd):
            # print(aux + proporcion[i])
            return i
        aux = aux + proporcion[i]        

def CalcularFitnness(X):
    rank = np.zeros(len(X))
    for i in range(len(X)):
        rank[i] = peso[i]/valor[i]
        
    indices_ordenados = np.argsort(rank)
    # print("desordenado: ", indices_ordenados)
    X = X[indices_ordenados]
    print("ordenado: ", X)
    return X

def algoritmo(tau):
    # Parametros
    # - Archivo de entrada
    # - Valor semilla
    # - Iteraciones
    # - Valor de Tao
    entrada, semilla, iteraciones, Tao, C = Parametros()

    # np.random.seed(semilla)

    # Inicializar Ecosistema
    #   - Generar una solucion inicial aleatoria
    X = np.zeros(len(archivo), dtype=np.int8)
    # # Aleatoriamente asignar algunos valores a 1
    for i in range(len(X)):
        X[i] = np.random.randint(0,2)
    # print(X)
    # # [1 0 1 1 1 1 0 0 1 1]

    #   - mejor solucion = solucion inicial
    X_best = X.copy()
    X_best_value, X_best_weight = EvaluarEcosistema(X_best)
    if(X_best_weight > C):
        X_best = np.ones(len(archivo))
        X_best = -X_best
        X_best_value = -1
        X_best_weight = np.inf

    #   - Generar un arreglo de probabilidad P siguiendo que P_i = i^-tao; para todo 1<= i <= n
    P = np.zeros(len(X))
    for i in range(1, len(P)+1):
        P[i-1] = round(i**(-tau),2)
    # print('arreglo Probabilidades: ', P)
    # arreglo Probabilidades:  [1., 0.38, 0.21, 0.14, 0.11, 0.08, 0.07, 0.05, 0.05, 0.04]
    #   - iterar _Iteraciones_: i
    #   - Evaluar y crear un ranking basado en el fitnes de cada valor de X_i del peor a mejor
    proporcion = np.array(P/sum(P))
    # print("proporcion: ", proporcion)
    i = 0
    while(i < iteraciones):
        print(i)
        # print("arreglo: ", X)
        X = CalcularFitnness(X).copy()
        
        seleccionado = Ruleta(proporcion)
        # print("seleccionado: ", seleccionado)
        
        new_value = np.random.randint(0,2)
        print(X[seleccionado])
        while(new_value == X[seleccionado]):
            new_value = np.random.randint(0,2)
        # print(X[new_value])    
        if(X[seleccionado] == -1):
            X[seleccionado] = 1
        else:
            X[seleccionado] = 1 - new_value
        #   - Seleccionar un componente j de X_i basado en la probabilidad del ranking P_i usando ¿RWS?
        #   - x_j = Generar un valor aleatorio que no sea igual a x_j
        X_value, X_weight = EvaluarEcosistema(X)
        if(X_value > X_best_value and X_weight <= C):
            X_best = X
            X_best_value = X_value
            print("valor: ", X_best)
            return X, X_best_value
        print("valor: ", X_weight)
        i += 1

def main():
    df = pd.DataFrame()
    taus = np.array([0.8, 1, 1.2, 1.4, 1.6, 1.8])
    semillas = 30
    for tau in taus:
        valores = list()
        for semilla in range(semillas):
            np.random.seed(semilla)
            array, mejor_solucion = algoritmo(tau)
            print("tau: ", tau, " semilla: ", semilla, " arreglo: ", array, " solucion: ", mejor_solucion)
            valores.append(mejor_solucion)

        df_temp = pd.DataFrame(valores, columns=['Mejor solucion factible'])
        df_temp['tau'] = tau
        df = pd.concat([df, df_temp])


if __name__ == '__main__':  
    main()

    