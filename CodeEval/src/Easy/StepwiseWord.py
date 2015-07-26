'''
Created on 26.07.2015

@author: Ivan Varus
'''

from sys import argv


def stepwise(s):
    return ' '.join(i*'*' + c for i, c in enumerate(s))


with open(argv[1], 'r') as tests:
    for t in tests:
        print(stepwise(max(t.split(), key=len)))
