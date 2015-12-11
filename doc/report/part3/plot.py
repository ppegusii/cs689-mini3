#!/usr/bin/env python
from __future__ import print_function
import json
import matplotlib.pyplot as plt
import sys


def main():
    with open(sys.argv[1], 'rb') as f:
        allData = json.load(f)
    for param, data in allData.items():
        x = data['x']
        y = data['y']
        if len(x) != len(y):
            print('Skipping {}'.format(param))
            continue
        xy = zip(x, y)
        xy.sort(key=lambda t: t[0])
        x, y = zip(*xy)
        if param == 'learning_rate' or param == 'experience_size':
            plotPerformance(x, y, param, log=True)
        else:
            plotPerformance(x, y, param)


def plotPerformance(x, y, x_label, log=False):
    plt.plot(x, y, marker='o', mfc='none', mec='red')
    if log:
        plt.xscale('log')
    plt.ylabel('average_reward')
    plt.xlabel(x_label)
    plt.ylim(ymin=0)
    plt.show()


if __name__ == '__main__':
    main()
