"""
This class represents a generation of robots with their associated values. 
It contains a list of the individuals form that generation.
"""

__author__ = 'Ali Hajimirza'
__copyright__ = "Copyright 2015, OU REAL LAB"
__license__ = "MIT"


import numpy as np

class Generation(object):
    def __init__(self, generation_number, individual_list):
        self.individual_list = np.array(individual_list)
        self.number = generation_number
        fitness_list = np.array([indi.fitness for indi in individual_list])
        self.max_fitness = np.amax(fitness_list)
        self.ave_fitness = np.mean(fitness_list)
        self.min_fitness = np.amin(fitness_list)

    def get_parents(self):
        return np.array([indi.parent_UUID for indi in self.individual_list])

    def __str__(self):
        return 'Generation Number: {}, Min Fitness: {}, Ave Fitness {}, Max Fitness: {}'.format(self.number, self.min_fitness, self.ave_fitness ,self.max_fitness)

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        return self.individual_list[index]
