import numpy as np
import random
from copy import deepcopy

class SudokuSolver:
    def __init__(self, target, population_size=1000, generations=5000, mutation_rate=0.2):
        self.target = target
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.fixed_positions = self._get_fixed_positions(target)
        self.population = self._initialize_population()
        print("Initialization complete")

    def _get_fixed_positions(self, board):
        fixed = np.zeros_like(board, dtype=bool)
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    fixed[i][j] = True
        print("Fixed positions identified:\n", fixed)
        return fixed

    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self._generate_individual()
            population.append(individual)
        print("Initial population generated")
        return population

    def _generate_individual(self):
        board = np.copy(self.target)
        for i in range(9):
            missing_nums = [num for num in range(1, 10) if num not in board[i]]
            random.shuffle(missing_nums)
            for j in range(9):
                if board[i][j] == 0:
                    board[i][j] = missing_nums.pop()
        return board

    def _fitness(self, board):
        score = 0
        for row in range(9):
            score += len(np.unique(board[row]))  # Unique numbers in the row
        for col in range(9):
            score += len(np.unique(board[:, col]))  # Unique numbers in the column
        for box_row in range(3):
            for box_col in range(3):
                box = board[box_row*3:(box_row+1)*3, box_col*3:(box_col+1)*3]
                score += len(np.unique(box))  # Unique numbers in the box
        return score

    def _crossover(self, parent1, parent2):
        child = np.copy(parent1)
        for i in range(9):
            if random.random() > 0.5:
                child[i] = parent2[i]
        return child

    def _mutate(self, child):
        for i in range(9):
            if random.random() < self.mutation_rate:
                swap_indices = [j for j in range(9) if not self.fixed_positions[i][j]]
                if len(swap_indices) >= 2:
                    idx1, idx2 = random.sample(swap_indices, 2)
                    child[i][idx1], child[i][idx2] = child[i][idx2], child[i][idx1]
        return child

    def solve(self):
        best_board = None
        best_fitness = 0

        for generation in range(self.generations):
            self.population = sorted(self.population, key=self._fitness, reverse=True)
            current_best_fitness = self._fitness(self.population[0])
            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                best_board = self.population[0]

            print(f"Generation {generation}: Best fitness = {best_fitness}")

            if best_fitness == 243:  # Each row, column, and box should have 9 unique numbers
                print("Optimal solution found!")
                break

            next_generation = self.population[:10]
            for _ in range(self.population_size - 10):
                parent1 = random.choice(self.population[:50])
                parent2 = random.choice(self.population[:50])
                child = self._crossover(parent1, parent2)
                child = self._mutate(child)
                next_generation.append(child)
            self.population = next_generation

            if generation % 100 == 0:  # Print board every 100 generations for debugging
                print(f"Generation {generation}: Best board so far\n{best_board}")

        return best_board, best_fitness

target = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

solver = SudokuSolver(target)
solution, solution_fitness = solver.solve()
print("سودوکوی حل شده:")
print(solution)
print("برازش:", solution_fitness)
