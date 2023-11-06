import numpy as np
import pandas as pd
import sys
import time

def Parametros():
    continue

def EvaluarEcosistema():
    continue

def Reemplazo():
    continue

def Ruleta():
    continue

def CalcularFitnness():
    continue

def main():
    # Parametros
    # - Archivo de entrada
    # - Valor semilla
    # - Iteraciones
    # - Valor de Tao

    # Generar numero randomico entre 0 y 1
    # Generar numero randomico entre 1 y N
    # Inicializar Ecosistema
    #   - Generar una solucion inicial aleatoria
    #   - mejor solucion = solucion inicial
    #   - Generar un arreglo de probabilidad P siguiendo que P_i = i^-tao; para todo 1<= i <= n
    #   - iterar _Iteraciones_: i
    #   - Evaluar y crear un ranking basado en el fitnes de cada valor de X_i del peor a mejor 
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

    print('esta funcionando con los paquetes')

if __name__ == '__main__':
    main()