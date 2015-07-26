'''
Created on 26.07.2015

@author: Ivan Varus
'''

import sys
from itertools import groupby

with open(sys.argv[1], 'r') as tests:
    for t in tests:
        group = groupby(t, key=lambda e: e.isalpha())
        s = ' '.join(''.join(g) for k, g in group if k)
        print(s.lower())
