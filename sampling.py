import numpy as np
from numpy.random import choice
from collections import Counter

from random import  sample

def weighted_sample(population, weights, k):
    """ 
    This function draws a random sample (without repeats) 
    of length k     from the sequence 'population' according 
    to the list of weights
    """
    sample = set()
    population = list(population)
    weights = list(weights)
    while len(sample) < k:
        choice1 = choice(population, weights)
        sample.add(choice1)
        index = population.index(choice1)
        weights.pop(index)
        population.remove(choice1)
        weights = [ x / sum(weights) for x in weights]
    return list(sample)
candies = ["red", "green", "blue", "yellow", "black", "white", "pink", "orange"]
weights = [ 1/24, 1/6, 1/6, 1/12, 1/12, 1/24, 1/8, 7/24]
for i in range(10):
    print(weighted_sample(candies, weights, 3))