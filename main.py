import numpy as np
from sys import argv as arg, exit
import pandas as pd 




def main():
    if len(arg) == 8:
        entrada = arg[1]
        semilla = int(arg[2])
        n_ants = int(arg[3])
        i = int(arg[4])
        f_ev = float(arg[5])
        c_h = float(arg[6])
        p_l = float(arg[7])
        print(entrada, semilla, n_ants, i, f_ev, c_h, p_l)
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


if __name__ == "__main__":
    main()