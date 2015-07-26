'''
Created on 26.07.2015

@author: Ivan Varus
'''

from sys import argv


def applymask(s, mask):
    return ''.join(c if k == '0' else c.upper()
                   for c, k in zip(s, mask))


with open(argv[1]) as tests:
    for t in tests:
        print(applymask(*t.split()))
