# README

## Problema de la Mochila

Este script de Python aborda el problema de la mochila utilizando un algoritmo genético simple. El problema de la mochila implica seleccionar un subconjunto de artículos de una lista, cada uno con un valor y un peso asociados, de modo que la suma de los pesos de los artículos seleccionados no supere una capacidad dada, y se maximice el valor total de los artículos seleccionados.

### Contenido del Archivo

- **main.py:** Contiene el código principal que implementa el algoritmo genético para resolver el problema de la mochila.
- **archivo de entrada** Archivo de entrada dentro de la carpeta _input_ que contiene información sobre los casos de prueba, incluyendo el número de artículos (N), la capacidad de la mochila (C), el valor óptimo (Z), y detalles sobre cada artículo.

### Funcionalidades Principales

1. **InitializeEcosystem:** Inicializa una población de soluciones aleatorias para el problema de la mochila.

2. **Probabilities:** Calcula las probabilidades para el proceso de selección de la ruleta mediante el valor de Tau y el tamaño de la mochila.

   $
   P_i = i^{-T} \quad \forall i \quad 1 \leq i \leq n
   $

3. **Roulette:** Realiza la selección de un individuo utilizando el método de la ruleta ponderada con las probabilidades de la funcion _Probabilities_.

4. **Replacement:** Realiza el reemplazo de un individuo en la población utilizando la selección de ruleta y ajustando la solución para cumplir con las restricciones de capacidad.

5. **Fitness:** Calcula la aptitud (fitness) de cada especie en el ecosistema.

6. **EvaluateEcosystem:** Evalúa el valor total de una solución para el problema de la mochila.

7. **DataBackpack:** Lee y procesa datos de entrada sobre casos de prueba desde un archivo.

8. **main:** Implementa el algoritmo genético para resolver el problema de la mochila utilizando diferentes valores de Tau y semillas.

### Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script principal `main.py` para ejecutar el algoritmo genético en el conjunto de datos proporcionado.

### Dependencias

- Se requieren las bibliotecas NumPy, Pandas, Seaborn y Matplotlib para la ejecución del script. Puedes instalar estas dependencias utilizando el siguiente comando:

  ```
  pip install numpy pandas seaborn matplotlib
  ```

### Configuración de Ejecución

- El script está configurado para ejecutarse con el conjunto de datos `knapPI_9_50_100000.csv` ubicado en la carpeta `input/large/`. Puedes cambiar el archivo de entrada en la sección `archivo_csv_large` del método `main` según sea necesario.

- El script también utiliza diferentes valores de Tau especificados en la lista `Tau` para explorar diferentes configuraciones del problema de la mochila.

### Resultados

El script generará resultados que incluyen soluciones óptimas encontradas para cada combinación de Tau y semilla, así como un gráfico de caja (boxplot) que compara el desempeño de diferentes valores de Tau.

## Créditos

Este proyecto fue desarrollado por Diego San Martín y Constanza Pérez como parte del curso Algoritmos Metaheuristicos Inspirados en la Naturaleza.
