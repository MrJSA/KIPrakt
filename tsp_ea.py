import numpy as np
import random

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def create_random_tour(n_cities):
    tour = list(range(n_cities))
    random.shuffle(tour)
    return tour

def swap_mutation(tour, mutation_rate):
    tour = tour.copy()
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    ptr = end
    for city in parent2:
        if city not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = city
            ptr += 1
    return child

def evolutionary_algorithm_tsp(distance_matrix, mu=50, lambd=100, generations=500, mutation_rate=0.1):
    n_cities = distance_matrix.shape[0]
    population = [create_random_tour(n_cities) for _ in range(mu)]
    best_tour = None
    best_distance = float("inf")
    history = []

    for gen in range(generations):
        offspring = []
        for _ in range(lambd):
            parents = random.sample(population, 2)
            child = order_crossover(parents[0], parents[1])
            child = swap_mutation(child, mutation_rate)
            offspring.append(child)

        combined = population + offspring
        combined.sort(key=lambda t: calculate_total_distance(t, distance_matrix))
        population = combined[:mu]

        dist = calculate_total_distance(population[0], distance_matrix)
        history.append(dist)

        if dist < best_distance:
            best_distance = dist
            best_tour = population[0]

        if gen % 50 == 0 or gen == generations - 1:
            print(f"Generation {gen}: Best distance = {best_distance:.2f}")

    return best_tour, best_distance, history
