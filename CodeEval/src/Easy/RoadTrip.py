'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys

f = open(sys.argv[1], 'r')
for line in f:
    chunks = line.split(';')
    if len(chunks) == 0:
        continue
    distances = []
    for chunk in chunks:
        citydistance = chunk.split(',')
        if len(citydistance) != 2:
            continue
        distances.append(int(citydistance[1]))
    add = 0
    deltas = []
    for d in sorted(distances):
        delta = d - add
        add += delta
        deltas.append(delta)
    print(','.join(str(d) for d in deltas))
f.close()
