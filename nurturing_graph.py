import json
import argparse
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from stat_generator import nurturing_count

arg_parser = argparse.ArgumentParser(description='Plot bar graph for number of nurturing events')
arg_parser.add_argument('config', type=argparse.FileType('rb'), help='Config file')
args = arg_parser.parse_args()
config = json.load(args.config)

output_paht = os.path.join('output', config['title'].replace(' ', '-'))
#If the values are specified
graph_format = 'pdf'
if 'format' in config:
    graph_format = config['format']

width = 0.15
if 'width' in config:
    width = config['width']

opacity = 0.4  
if 'opacity' in config:
    opacity = config['opacity']

color = ['r', 'g', 'b', 'c', 'k', 'y', 'm']
if 'color' in config:
    color = config['color']

# Calculating the result
xlabel = list()
data_arrays = list()
ind = np.arange(len(config['data']))
for data in config['data']:
    sys.stdout.write('Reading {}\n'.format(data['src']))
    cum_sum, num_trials = nurturing_count.count(data['src'])
    data_arrays.append(cum_sum[:,-1])
    xlabel.append(data['label'])

# Chisquare test and metadata output
data_arrays =  np.array(data_arrays)
with open(output_paht + '.txt', 'wb') as output_metafile:
    output_metafile.write('count array\n {}\n\n'.format(data_arrays))
    try:
        stat, p_val = map(np.sum, chisquare(data_arrays))
        output_metafile.write('Statistic: {}, P value: {}\n'.format(stat, p_val))
        if p_val:
            output_metafile.write('Chisquare Test: ' + 'Passed' if p_val < 0.05 else 'Failed')
    except Exception as e:
        sys.stderr.write('Failed to run chisquare test {}\n'.format(e))
        output_metafile.write('Failed to run chisquare test {}\n'.format(e))


# Creating the graph
fig, ax = plt.subplots()
ax.set_ylabel(config['ylabel'])
ax.set_title(config['title'])
ax.set_xticklabels(xlabel)
ax.set_xticks(ind + width)
plots = list()
data_arrays = np.divide(data_arrays, num_trials, dtype=np.float)
for i, data in enumerate(data_arrays.transpose()):
    plots.append(ax.bar(ind+(i*width), data, width, alpha=opacity, color=color[i])[0])
ax.legend(plots, config['legend'])

#Saving to a file
with open(output_paht + '.'+ graph_format, 'wb') as output_graph:
    plt.savefig(output_graph, format=graph_format)




