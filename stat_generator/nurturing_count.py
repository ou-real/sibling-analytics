from os import path
import sys
sys.path.append(path.dirname(path.realpath(path.join(__file__, '../'))))

import numpy as np
from objects import parser

def count(trial_path):
    num_trials = 0
    cum_nurturing = list()
    for trial in parser.get_trial_list(trial_path):
        if not num_trials:
            cum_nurturing = np.zeros((3, trial.num_generations))
        num_trials += 1

        pop_size = trial.config['populationSize']
        for generation in trial:
            for i in xrange(pop_size):
                a, b = generation[i], generation[i + pop_size]

                if a.light_first or b.light_first:
                    # A nurtured B
                    if b.light_first and a.switch and a <= b:
                        cum_nurturing[0][generation.number] += 1
                    # B nurtured A
                    elif a.light_first and b.switch and a >= b: 
                        cum_nurturing[0][generation.number] += 1
                    # Self care    
                    else:
                        cum_nurturing[1][generation.number] += 1

                # Self care
                elif a.switch or b.switch:
                    if (a.fitness != 0) or (b.fitness != 0):
                        cum_nurturing[1][generation.number] += 1
                    else:
                        cum_nurturing[2][generation.number] += 1

                elif (a.fitness == 0) and (b.fitness == 0):
                    cum_nurturing[2][generation.number] += 1

                else:
                    cum_nurturing[2][generation.number] += 1
                    print 'Warning Case else: {}   {}'.format(a, b)
    return cum_nurturing, num_trials

if __name__ == '__main__':
    print count('/Users/AliHM/Documents/workspace/nevil/sibling-analytics/results/case_1')