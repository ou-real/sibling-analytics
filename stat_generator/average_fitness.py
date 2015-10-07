from os import path
import sys
sys.path.append(path.dirname(path.realpath(path.join(__file__, '../'))))

from objects import parser
import numpy as np

def compute_avg(trial_path, overall=True):
    num_trials = 0
    cum_fitness = list()
    for trial in parser.get_trial_list(trial_path):
        # Only initialize the array on the first iteration
        if not num_trials:
            cum_fitness = np.zeros((2, trial.num_generations))
        num_trials += 1

        if overall:
            for generation in trial:
                cum_fitness[0][generation.number] += generation.max_fitness
                cum_fitness[1][generation.number] += generation.ave_fitness
        else:
            for generation in trial:
                selected_fitness = [i.fitness for i in generation if i.selected]
                if selected_fitness:
                    cum_fitness[0][generation.number] += np.amax(selected_fitness)
                    cum_fitness[1][generation.number] += np.mean(selected_fitness)

    return np.divide(cum_fitness, num_trials, dtype=np.float)
