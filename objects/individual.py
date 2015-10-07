"""
This class represents an individual robot with its associated values.
"""

__author__ = 'Ali Hajimirza'
__copyright__ = "Copyright 2015, OU REAL LAB"
__license__ = "MIT"

class Individual(object):
    def __init__(self, UUID, parent_UUID, switch, light_first, fitness, selected=False):
        self.UUID = UUID
        self.parent_UUID = parent_UUID
        self.switch = switch
        self.light_first = light_first
        self.selected = selected
        self.fitness = fitness

    def is_A(self):
        return self.UUID.endswith('A')

    def is_B(self):
        return self.UUID.endswith('B')

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness        

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness   

    def __eq__(self, other):
        return self.UUID == other.UUID

    def __ne__(self, other):
        return self.__eq__(other)

    def __str__(self):
        string = 'P:{} C:{} F:{} '.format(self.parent_UUID, self.UUID, self.fitness)
        if self.switch:
            string += 'Switch '
        if self.light_first:
            string += 'Light-First '
        if self.selected:
            string += 'Selected'
        return string.strip()

    def __repr__(self):
        return str(self)