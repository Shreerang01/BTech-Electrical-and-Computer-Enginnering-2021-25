#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:



def fitness_function(individual):
    return sum(individual)

def generate_individual():
    return [random.randint(0, 100) for _ in range(10)]

def mutate(individual):
    index_to_mutate = random.randint(0, len(individual) - 1)
    individual[index_to_mutate] = random.randint(0, 100)
    return individual

def crossover(parent1, parent2):
    midpoint = len(parent1) // 2
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]

    return child1, child2

def select_parents(population):
    fitness_values = [fitness_function(ind) for ind in population]
    total_fitness = sum(fitness_values)
    probabilities = [fit / total_fitness for fit in fitness_values]
    parents = []
    for _ in range(2):
        selected_parents = random.choices(population, probabilities, k=2)
        parents.append(max(selected_parents, key=fitness_function))
    return parents

def genetic_algorithm():
    population_size = 100
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(100):
        parents = select_parents(population)
        offspring = []

        for i in range(population_size // 2):
            parent1, parent2 = parents
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutate(child1))
            offspring.append(mutate(child2))

        population = parents + offspring
        population.sort(key=fitness_function, reverse=True)
        population = population[:population_size]

    return population[0]


# In[3]:


best_individual = genetic_algorithm()
print("Best Individual:", best_individual)
print("Fitness Value:", fitness_function(best_individual))


# In[ ]:




