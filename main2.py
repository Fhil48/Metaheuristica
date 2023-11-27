import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
def leer_archivo_csv(nombre_archivo):
    casos = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        i = 0
        while i < len(lineas):
            while i < len(lineas) and not lineas[i].strip().startswith("knap"):
                i += 1
            if i >= len(lineas):
                break
            
            nombre_caso = lineas[i].strip()
            i += 1

            n = int(lineas[i].split()[1])
            c = int(lineas[i+1].split()[1])
            z = int(lineas[i+2].split()[1])
            tiempo = float(lineas[i+3].split()[1])

            datos_caso = np.zeros((n, 4), dtype=int)

            for j in range(n):
                datos = list(map(int, lineas[i+4+j].split(',')))
                datos_caso[j,:] = datos
            
            casos.append({
                'Nombre': nombre_caso,
                'N': n,
                'C': c,
                'Z': z,
                'tiempo': tiempo,
                'datos': datos_caso,
            })


            while i < len(lineas) and not lineas[i].strip().startswith("-----"):
                i += 1
            i += 1
    return casos

def solucion_inicial(n, datos_caso, capacidad):
    x = np.zeros(n, dtype=int)
    for i in np.argsort(-datos_caso[:, 1] / datos_caso[:, 2]):
        if datos_caso[i, 1] <- capacidad:
            x[i] = 1
            capacidad -= datos_caso[i, 1]
    return x

def generar_probabilidades(n, tau):
    probabilidades = np.array([(i+1) ** -tau for i in range(n)])
    probabilidades /= np.sum(probabilidades)
    return probabilidades

def seleccionar_componente(probabilidades):
    seleccionado = np.random.choice(len(probabilidades), p = probabilidades)
    return seleccionado

def evaluar_solucion(solucion, datos_caso):
    evaluacion = np.sum(solucion*datos_caso[:,1])
    return evaluacion

def generar_nueva_solucion(solucion, componente_seleccionado, datos_caso, capacidad):
    nueva_solucion = solucion.copy()
    nueva_solucion[componente_seleccionado] = 1 - nueva_solucion[componente_seleccionado]

    while np.sum(nueva_solucion * datos_caso[:, 2]) > capacidad:
        objetos_incluidos = np.where(nueva_solucion == 1)[0]

        if len(objetos_incluidos) == 0:
            break
        
        objeto_a_quitar = objetos_incluidos[np.argmin(datos_caso[objetos_incluidos, 1])]

        nueva_solucion[objeto_a_quitar] = 0

    return nueva_solucion

def algoritmo(caso, num_interaciones, tau):
    mejor_solucion = solucion_inicial(caso['N'], caso['datos'], caso['C'])
    mejor_evaluacion = evaluar_solucion(mejor_solucion, caso['datos'])

    for e in range(num_interaciones):
        probabilidades = generar_probabilidades(caso['N'], tau)

        fitness = [evaluar_solucion(mejor_solucion, caso['datos']) for a in range(caso['N'])]
        indices_ordenados = np.argsort(fitness)[::-1]

        for i in range(caso['N']):
            componente_seleccionado = seleccionar_componente(probabilidades)

            nueva_solucion = generar_nueva_solucion(mejor_solucion, componente_seleccionado, caso['datos'], caso['C'])

            nueva_evaluacion = evaluar_solucion(nueva_solucion, caso['datos'])

            if nueva_evaluacion > mejor_evaluacion and np.sum(nueva_solucion * caso['datos'][:, 2]) <= caso['C']:
                mejor_solucion = nueva_solucion
                mejor_evaluacion = nueva_evaluacion
    return mejor_solucion, mejor_evaluacion 

def main():
    tau_values = [0.8, 1, 1.2, 1.4, 1.6, 1.8]
    iteraciones = 1000
    archivo_csv = 'input/knapPI_9_50_1000.csv'
    semillas = 30
    casos = leer_archivo_csv(archivo_csv)

    df = pd.DataFrame()

    for tau in tau_values:
        valores = list()
        for semilla in range(semillas):
            np.random.seed(semilla)
            array, mejor_solucion = algoritmo(casos[3], iteraciones, tau)
            print("tau: ", tau, " semilla: ", semilla, " arreglo: ", array, " mejor solucion factible: ", mejor_solucion, " de: ", casos[3]['Z'])
            valores.append(mejor_solucion)
        df_temp = pd.DataFrame(valores, columns=['mejor_solucion'])
        df_temp['tau'] = tau
        df = pd.concat([df, df_temp])
    sns.boxplot(x='tau', y='mejor_solucion', data=df)

if __name__ == "__main__":
    main()