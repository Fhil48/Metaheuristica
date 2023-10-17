import numpy as np
from sys import argv as arg, exit
import pandas as pd 


def parametros():
    if len(arg) == 8:
        entrada = arg[1]
        semilla = int(arg[2])
        n_ants = int(arg[3])
        i = int(arg[4])
        f_ev = float(arg[5])
        c_h = float(arg[6])
        p_l = float(arg[7])
        return entrada, semilla, n_ants, i, f_ev, c_h, p_l
    else:
        print("Error en los parametros de entrada")
        print("Los parametros a ingresar son: Archivo de entrada, semilla, numero de hormigas, iteraciones, Factor de evaporacion, coeficiente heuristico, valor probabilidad limite")
        print("archivo de entrada: berlin52")
        print("semilla: numero entero")
        print("numero de hormigas: 10-100")
        print("iteraciones: 100-500")
        print("Factor de evaporacion: 0.1")
        print("Coeficiente heuristico: 2-5")
        print("Probabilidad limite: 0.9")
        exit(0)
def solucionCalculoCosto(numeroVariables, solucionMejor, matrizDistancias):
    aux = matrizDistancias[solucionMejor[numeroVariables-1]][solucionMejor[0]]
    for i in range(numeroVariables-1):
        aux += matrizDistancias[solucionMejor[i]][solucionMejor[i+1]]
    return aux

def main():
    entrada, semilla, n_ants, i, f_ev, c_h, p_l = parametros()
    print(entrada, semilla, n_ants, i, f_ev, c_h, p_l)

    # Matriz con coordenadas x,y obtenida del archivo berlin52
    matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
    matrizCoordenadas = matrizCoordenadas.drop(columns=0, axis=1).to_numpy()
    numVariables = matrizCoordenadas.shape[0]
    print(matrizCoordenadas)

    # matriz de distancia entre cada vertice del grafo que representa la matriz
    matrizDistancias = np.full((numVariables, numVariables), fill_value = -1.0, dtype = float)
    for i in range(numVariables-1):
        for j in range(i+1, numVariables):
            matrizDistancias[i][j] = np.sqrt(np.sum(np.square(matrizCoordenadas[i]-matrizCoordenadas[j])))
            matrizDistancias[j][i] = matrizDistancias[i][j]
    print('Matriz de Distancia:\n', matrizDistancias, '\ntamaño:', matrizDistancias.shape, '\ntipo:', type(matrizDistancias))

    matrizHeuristica = np.full_like(matrizDistancias, fill_value = 1/matrizDistancias, dtype = float)
    np.fill_diagonal(matrizHeuristica, 0)
    print('Matriz de Heuristicas:\n', matrizHeuristica, '\ntamaño:', matrizHeuristica.shape, '\ntipo:', type(matrizHeuristica))
    


    
if __name__ == "__main__":
    main()
