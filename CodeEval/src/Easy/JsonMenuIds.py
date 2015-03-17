'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys
import json


def addLabels(target, add):
    if isinstance(target, dict):
        if 'label' in target:
            add[0] += target.get('id', 0)
        for v in target.values():
            addLabels(v, add)
    elif isinstance(target, list) or isinstance(target, tuple):
        for x in target:
            addLabels(x, add)


f = open(sys.argv[1], 'r')
for line in f:
    if not line.strip():
        continue
    D = json.loads(line)
    add = [0]  # mutable !
    addLabels(D, add)
    print(add[0])
f.close()
