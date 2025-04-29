import random

def generate_population(size):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 7) for _ in range(8)]
        population.append(individual)
    return population

def calculate_fitness(individual):
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return 28 - conflicts  # 28 is the maximum fitness score achievable

def select_parents(population):
    total_fitness = sum(calculate_fitness(individual) for individual in population)
    probabilities = [calculate_fitness(individual) / total_fitness for individual in population]
    parent1 = random.choices(population, weights=probabilities)[0]
    parent2 = random.choices(population, weights=probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 7)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(8):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, 7)
    return individual

def genetic_algorithm(population_size, mutation_rate, generations):
    population = generate_population(population_size)
    for gen in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        best_individual = max(population, key=calculate_fitness)
        if calculate_fitness(best_individual) == 28:
            return best_individual, gen
    best_individual = max(population, key=calculate_fitness)
    return best_individual, generations

def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def main():
    print("Enter the initial positions of queens (0-7) for each row:")
    initial_board = []
    for i in range(8):
        position = int(input(f"Row {i}: "))
        initial_board.append(position)

    population_size = 100
    mutation_rate = 0.1
    generations = 1000

    solution, gen_count = genetic_algorithm(population_size, mutation_rate, generations)
    print("Solution Found:")
    print_board(solution)
    print(f"Solution found in generation: {gen_count}")

if __name__ == "__main__":
    main()
