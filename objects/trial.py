"""
This class represents an experiment with a number of generations.
It contains a list of the generations for that experiment and other information.
"""

__author__ = 'Ali Hajimirza'
__copyright__ = "Copyright 2015, OU REAL LAB"
__license__ = "MIT"

import numpy as np

class Trial(object):
    def __init__(self, config, generation_list):
        self.config = config
        self.generation_list = np.array(generation_list)
        self.num_generations = len(generation_list)
        # Set the ones who where selected
        for i in xrange(1, len(self.generation_list)):
            parents = self.generation_list[i].get_parents()
            for ind in self.generation_list[i-1]:
                if ind.UUID in parents:
                    ind.selected = True

    def __str__(self):
        trial_str = 'TrialName: {}\n'.format(self.config['trialName'])
        for key, val in self.config.iteritems():
            if (key != 'trialName'):
                trial_str += '{} : {}\n'.format(key, val)
        return trial_str


    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        return self.generation_list[index]