'''
Created on 26.07.2015

@author: Ivan Varus
'''

from sys import argv


with open(argv[1]) as tests:
    for t in tests:
        print(' '.join(w[-1] + w[1:-1] + w[0] for w in t.split()))
