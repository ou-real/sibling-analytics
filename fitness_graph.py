import json
import argparse
import itertools
import os
import sys
import matplotlib.pyplot as plt
from matplotlib import gridspec
from stat_generator import average_fitness

arg_parser = argparse.ArgumentParser(description='Plot line graph for a set of trials')
arg_parser.add_argument('config', type=argparse.FileType('rb'), help='Config file')
args = arg_parser.parse_args()
config = json.load(args.config)

output_paht = os.path.join('output', config['title'].replace(' ', '-'))
GS = gridspec.GridSpec(1, 1, width_ratios=[7, 2], height_ratios=[10,1]) 
#If the values are specified
graph_format = 'pdf'
if 'format' in config:
    graph_format = config['format']

markers = [ '',  '--' ,'+' ,'s' , '*' ,'d', '.' ,'v', 'p', ',' ,'o', '^', 'x']
if 'markers' in config:
    markers = config['markers']

color = ['r', 'g', 'b', 'c', 'k', 'y', 'm']
if 'color' in config:
    color = config['color']


# Creating the graph
graphs = list()
labels = list()
plt.subplot(GS[0])
for data, c in itertools.izip(config['data'], color):
    fitness_avg = average_fitness.compute_avg(data['src'], overall=data['overall'])
    labels.extend(data['label'])
    for value, m in itertools.izip(fitness_avg, markers):
        graphs.append(plt.plot(value, m, color=c)[0])
plt.legend(graphs, labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.suptitle(config['title'], fontsize=14)
plt.xlabel(config['xlabel'])
plt.ylabel(config['ylabel'])

#Saving to a file
with open(output_paht + '.'+ graph_format, 'wb') as output_graph:
    plt.savefig(output_graph, format=graph_format)