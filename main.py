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

def ruleta(array_prob, neighbor):
    suma = 0
    aleatorio = np.random.random()

    for i, prob in enumerate(array_prob):
        suma += prob
        if (aleatorio <= suma):
            return neighbor[i]

def solucionCalculoCosto(numeroVariables, solucionMejor, matrizDistancias):
    aux = matrizDistancias[solucionMejor[numeroVariables-1]][solucionMejor[0]]
    for i in range(numeroVariables-1):
        aux += matrizDistancias[solucionMejor[i]][solucionMejor[i+1]]
    return aux

def main():
    entrada, semilla, n_ants, iteraciones, f_ev, c_h, p_l = parametros()
    print(entrada, semilla, n_ants, iteraciones, f_ev, c_h, p_l)
    np.random.seed(semilla)
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
    
     # Solucion Optima
    solucionOptima = pd.read_table('berlin52.opt.tour.txt', header = None, skiprows = 4, skipfooter = 2).to_numpy().flatten()
    solucionOptima -= 1
    print('Mejor solucion:\n', np.sort(solucionOptima))

    # Solucion inicial
    solucionInicial = np.arange(0, numVariables)
    np.random.shuffle(solucionInicial)
    costoSolucionInicial = solucionCalculoCosto(numVariables, solucionInicial, matrizDistancias)
    print('Costo solucion Inicial: ', costoSolucionInicial)
    #  [1, 49, 32, 45, 19, 41, 8, 9, 10, 43, 33, 51, 11, 52, 14, 13, 47, 26, 27, 28, 12, 25, 4, 6, 15, 5, 24, 48, 38, 37, 40, 39, 36, 35, 34, 44, 46, 16, 29, 50, 20, 23, 30, 2, 7, 42, 21, 17, 3, 18, 31, 22]
    # Inicializar Feromonas 
    T_ij0 = 1/(numVariables*costoSolucionInicial)
    matrizFeromonas = np.full((numVariables, numVariables), fill_value = T_ij0, dtype = float)
    np.fill_diagonal(matrizFeromonas, 0)
    print('Arreglo Feromonas:\n', matrizFeromonas)
    
    # Hormigas
    hormigas = np.empty(n_ants, dtype = object)
    hormigas[:] = [[] for i in range(n_ants)]

    costoSolucionActual = costoSolucionInicial        
    solucionActual = solucionInicial
    # Ciclo principal
    generacion = 0
    while generacion < iteraciones and not (np.round(costoSolucionActual, decimals=4) == 7544.3659):
        print('iteracion: ',generacion)
        # Inicializar cada hormiga en un nodo aleatorio
        hormigas = np.empty(n_ants, dtype = object)
        hormigas[:] = [[] for i in range(n_ants)]
        for ant in range(len(hormigas)):
            if ant < numVariables:
                hormigas[ant].append(ant)
            else:
                hormigas[ant].append(np.random.randint(0, numVariables))
        
        # Cada vertice del grafo
        for i in range(numVariables-1):
            # Cada hormiga
            for ant in hormigas:
                j0 = -np.inf
                max = -np.inf
                neighbor = np.array([x for x in range(numVariables) if x not in ant])
                if(np.random.random() < p_l):
                    for j in neighbor:
                        if(matrizFeromonas[ant[-1]][j]*matrizHeuristica[ant[-1]][j]**c_h > max):
                            max = matrizFeromonas[ant[-1]][j]*matrizHeuristica[ant[-1]][j]**c_h 
                            j0 = j
                    # ant.append(j0)
                else:
                    value = []
                    suma = 0
                    for j in neighbor:
                        prob = matrizFeromonas[ant[-1]][j]*matrizHeuristica[ant[-1]][j]**c_h
                        value.append(prob)
                        suma += prob
                        
                    prop = [j / suma for j in value]
                    j0 = ruleta(prop, neighbor)
                    # ant.append(j0)
                # Actualizar feromonas
                matrizFeromonas[ant[-1]][j0] = (1-f_ev)*matrizFeromonas[ant[-1]][j0]+f_ev*T_ij0
                ant.append(j0)
        for ant in hormigas:
            # print('costo: ', solucionCalculoCosto(numVariables, ant, matrizDistancias))
            if(costoSolucionActual > solucionCalculoCosto(numVariables, ant, matrizDistancias)):
                costoSolucionActual = solucionCalculoCosto(numVariables, ant, matrizDistancias)
                solucionActual = ant
        for v in range(len(solucionActual) - 1):
            nodo_actual = solucionActual[v]
            nodo_siguiente = solucionActual[v+1]
            matrizFeromonas[nodo_actual][nodo_siguiente] = (1-f_ev)*matrizFeromonas[nodo_actual][nodo_siguiente] + f_ev*(1/costoSolucionActual) 

        # print('iteracion cosots: ', costoSolucionActual)
        # print('iteracion: ', solucionActual)

        generacion += 1
    print('mejor Solucion inicial', solucionInicial)
    print('costo inicial Solucion', costoSolucionInicial)
    print('mejor Solucion', solucionActual)
    print('costo mejor Solucion', costoSolucionActual)
    # Imprimir camino hormigas    
    # for ant in hormigas:    
    #     print('hormiga:',np.sort(ant))
    # Ver camino de hormigas        


if __name__ == "__main__":
    main()
