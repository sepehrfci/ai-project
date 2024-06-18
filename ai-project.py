import numpy as np
import random

# Define the fitness function
def fitness(board, target):
    fitness = 0
    for i in range(9):
        row = board[i, :]
        col = board[:, i]
        fitness += len(set(row)) + len(set(col))
    fitness -= 9  # Subtract the overcounted rows and columns
    return fitness

# Generate a random Sudoku board
def generate_board():
    board = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            if random.random() < 0.3:
                board[i, j] = random.randint(1, 9)
    return board

# Perform crossover between two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(0, 8)
    child = np.vstack((parent1[:crossover_point], parent2[crossover_point:]))
    return child

# Perform mutation on a child
def mutate(child):
    for i in range(9):
        if random.random() < 0.1:
            child[i, random.randint(0, 8)] = random.randint(1, 9)
    return child

# Genetic Algorithm to solve Sudoku
def genetic_algorithm(target, generations=500, population_size=100):
    population = [generate_board() for _ in range(population_size)]
    best_board = None
    best_fitness = 0
    
    for generation in range(generations):
        population = sorted(population, key=lambda board: fitness(board, target), reverse=True)
        if fitness(population[0], target) > best_fitness:
            best_fitness = fitness(population[0], target)
            best_board = population[0]
        if best_fitness == 2 * 9 * 9:
            break
        next_generation = population[:10]
        for _ in range(population_size - 10):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        population = next_generation
    
    return best_board, best_fitness

# Target Sudoku board
print("Sudoku:")
target = generate_board()
print(target)
solution, solution_fitness = genetic_algorithm(target)
print("Solved Sudoku:")
print(solution)
print("Fitness:", solution_fitness)
