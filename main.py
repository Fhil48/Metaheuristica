import numpy as np
import pandas as pd
import sys
import time

def Parametros():
    pass

def EvaluarEcosistema():
    pass

def Reemplazo():
    pass

def Ruleta(proporcion):
    rd = np.random.random(1)
    print("rd: ", rd)
    aux = proporcion[0]
    for i in range(0,len(proporcion)-1):
        if(aux > rd):
            return i+1
        aux += proporcion[i+1]        
# Arreglar ruleta suma el primer indice cuando no deberia
def CalcularFitnness():
    pass

def main():
    # Parametros
    # - Archivo de entrada
    # - Valor semilla
    # - Iteraciones
    # - Valor de Tao
    entrada, semilla, iteraciones, Tao = 10, 1, 100, 1.4
    # entrada, semilla, iteraciones, Tao = Parametros(sys.argv)
    np.random.seed(semilla)
    # Generar numero randomico entre 0 y 1
    np.random.randint(0,2)
    # Generar numero randomico entre 1 y N
    np.random.randint(0, entrada+1)

    # Inicializar Ecosistema
    #   - Generar una solucion inicial aleatoria
    X = np.zeros(entrada, dtype=np.int8)
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
    #   - Representacion formal del problema
    #   - Maximizar 1<= i <= n; v_i * x_i 
    #   - donde 1<= i <= n; p_i * x_i <= C
    #   - x_i = {0, 1}
    #   - v_i = valor monetario del elemento i
    #   - x_i = variable de desicion, 1 si el elemento se encuentra en la mochila, 0 en otro caso.
    #   - p_i = el peso del elemento i
    #   - C = capacidad de peso en la mochila


    #  ¡FALTA!
    # Agregar descripcion de la foto sacada en clases


if __name__ == '__main__':
    main()