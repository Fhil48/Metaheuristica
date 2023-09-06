import random


def fitness(board):
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1

    return conflicts


def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(board):
    n = len(board)
    mutation_point = random.randint(0, n - 1)
    new_position = random.randint(0, n - 1)
    board[mutation_point] = new_position
    return board


def genetic_algorithm(n, population_size, generations):
    population = [[random.randint(0, n - 1) for _ in range(n)]
                  for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda board: fitness(board))
        # El mejor individuo pasa directamente
        new_population = [population[0]]

        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)

            if random.random() < 0.1:  # Probabilidad de mutación
                child = mutate(child)

            new_population.append(child)

        population = new_population

    return population[0]


def print_board(board):
    n = len(board)
    for row in range(n):
        print(" ".join("Q" if board[row] == col else "." for col in range(n)))


n = 12  # Cambiar este valor para el número deseado de reinas
population_size = 100
generations = 1000
solution = genetic_algorithm(n, population_size, generations)
print_board(solution)
