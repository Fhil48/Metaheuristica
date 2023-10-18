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
    np.random.seed(semilla)
    # Matriz con coordenadas x,y obtenida del archivo berlin52
    matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
    matrizCoordenadas = matrizCoordenadas.drop(columns=0, axis=1).to_numpy()
    numVariables = matrizCoordenadas.shape[0]
    print(matrizCoordenadas)
    
    # mejor solucion
    solucionMejor = pd.read_table('berlin52.opt.tour.txt', header = None, skiprows = 4, skipfooter = 2).to_numpy().flatten()
    print('Mejor solucion:\n', solucionMejor)
    #  [1, 49, 32, 45, 19, 41, 8, 9, 10, 43, 33, 51, 11, 52, 14, 13, 47, 26, 27, 28, 12, 25, 4, 6, 15, 5, 24, 48, 38, 37, 40, 39, 36, 35, 34, 44, 46, 16, 29, 50, 20, 23, 30, 2, 7, 42, 21, 17, 3, 18, 31, 22]
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
    
    # Feromonas
    feromonas = np.full(matrizCoordenadas.shape[0], fill_value = 0.01, dtype = float)
    print('Arreglo Feromonas:\n', feromonas)

    # Hormigas
    hormigas = np.empty(n_ants, dtype = object)
    hormigas[:] = [[] for i in range(n_ants)]

    # Inicializar cada hormiga en un nodo aleatorio
    nodes = np.arange(numVariables)
    np.random.shuffle(nodes)
    print('tamaño:\n')
    for i in range(len(hormigas)):
        if(i > len(nodes)-1):
            j = np.math.floor(np.random.randint(0, len(nodes)-1))
        else:
            j = i
        hormigas[i].append(nodes[j])
    print('Arreglo hormigas:\n', hormigas)
    
    for i in range(iteraciones):
        # for j in hormigas:
        for a in range(len(hormigas)):
            if(a > len(nodes)-1):
                j = np.math.floor(np.random.randint(0, len(nodes)-1))
            else:
                j = a
            hormigas[a].append(nodes[j])
        for j in hormigas:
            # Seleccionar proximo segmento
            # actualizar la feromona en el segmento
            if(np.random.random() < p_l):
                
            else:
    
if __name__ == "__main__":
    main()
