'''
Created on 26.07.2015

@author: Ivan Varus
'''

from sys import argv


def cmp(a, b):
    return (a > b) - (a < b)


with open(argv[1]) as tests:
    for t in tests:
        o, p, q, r = map(int, t.split())
        s = ['', 'S', 'N'][cmp(p, r)] + ['', 'W', 'E'][cmp(o, q)]
        print(s if s else 'here')
