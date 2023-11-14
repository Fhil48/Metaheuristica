import numpy as np
import pandas as pd
import sys
import time

def Parametros():
    # entrada = sys.argv[1]
    # semilla = sys.argv[2]
    # i = sys.argv[3]
    # T = sys.argv[4]
    #entrada = sys.argv[1]
    file_path = './input/knapPI_9_50_1000.csv'
    semilla = 1
    file = pd.read_csv(file_path, header=None, skiprows=1, nrows=2, delim_whitespace=True)
    i = file.iloc[0, 1]
    c = file.iloc[1, 1]    
    T = 1.4
    return file_path, semilla, i, T, c

def EvaluarEcosistema():
    pass

def Reemplazo():
    pass

def Ruleta(proporcion):
    rd = np.random.random(1)
    print("rd: ", rd)
    aux = 0
    for i in range(0,len(proporcion)-1):
        if(aux + proporcion[i] > rd):
            print(aux + proporcion[i])
            return i
        aux = aux + proporcion[i]        

def CalcularFitnness():
    pass

def main():
    # Parametros
    # - Archivo de entrada
    # - Valor semilla
    # - Iteraciones
    # - Valor de Tao
    entrada, semilla, iteraciones, Tao, C = Parametros()

    archivo = pd.read_csv(entrada, skiprows=5, header=None, nrows=50)

    peso = np.zeros(50)
    valor = np.zeros(50)
    for i, a in archivo.iterrows():
        peso[i] = a[1]
        valor[i] = a[2]
    # print('pesos: ', peso)
    # print('valores: ', valor)
    # for i in range(iteraciones):
    #     print('fitnes de item #', i , ', es: ', peso[i] * valor[i])

    # entrada, semilla, iteraciones, Tao = Parametros(sys.argv)
    np.random.seed(semilla)
    # Generar numero randomico entre 1 y N
    #np.random.randint(0, entrada+1)
    
    # Inicializar Ecosistema
    #   - Generar una solucion inicial aleatoria
    X = np.zeros(i, dtype=np.int8)
    # # Aleatoriamente asignar algunos valores a 1
    for i in range(len(X)):
        X[i] = np.random.randint(0,2)
    print(X)
    # # [1 0 1 1 1 1 0 0 1 1]

    #   - mejor solucion = solucion inicial
    X_best = X
    #   - Generar un arreglo de probabilidad P siguiendo que P_i = i^-tao; para todo 1<= i <= n
    P = np.zeros(len(X))
    for i in range(1, len(P)+1):
        P[i-1] = round(i**(-Tao),2)
    print('arreglo Probabilidades: ', P)
    # arreglo Probabilidades:  [1., 0.38, 0.21, 0.14, 0.11, 0.08, 0.07, 0.05, 0.05, 0.04]
    #   - iterar _Iteraciones_: i
    #   - Evaluar y crear un ranking basado en el fitnes de cada valor de X_i del peor a mejor 
    proporcion = np.array(P/sum(P))
    print("proporcion: ", proporcion)
    seleccionado = Ruleta(proporcion)
    print("seleccionado: ", seleccionado)
    #   - Seleccionar un componente j de X_i basado en la probabilidad del ranking P_i usando ¿RWS?
    #   - x_j = Generar un valor aleatorio que no sea igual a x_j
    #   - Evaluar el nuevo X
    #   - comparar X con el mejor X, e intercambiarlos si es asi
    #   - Devolver el mejor X y el valor de evaluar este X
    #   -------------- 

if __name__ == '__main__':
    main()

    