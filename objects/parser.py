import glob
import json
import os
import numpy as np

from individual import Individual
from generation import Generation
from trial import Trial

__version__ = "0.0.1"
__email__ = "ali@alihm.net"
__status__ = "Development"

def parse_trial(trial_path):
    with open(trial_path,'rb') as input_file:
        trial_result = json.load(input_file)
        generation_list = list()
        for gen in trial_result['generationalData']:
            individual_list = list()
            for indi in gen['individualList']:
                individual_list.append(
                    Individual(indi['UUID'], indi['parentUUID'], indi['switch'], indi['lightFirst'], indi['fitness']))

            generation_list.append(Generation(gen['generationNumber'], individual_list))

        trial = Trial(trial_result['config'], generation_list)
    return trial

def get_trial_list(trial_path):
    trial_path = os.path.abspath(trial_path)
    if not os.path.exists(trial_path):
        raise Exception('Trial path "{}" does not exists'.format(trial_path))
    for trial_path in glob.glob(os.path.join(trial_path,'*.json')):
        yield parse_trial(trial_path)