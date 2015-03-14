'''
Created on Mar 1, 2015

@author: Ivan Varus

Credits to Will Ness and others
'''

import sys
import itertools


def psieve():
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.rstrip()
    if not pretty:
        continue
    n = int(pretty)
    for prime in itertools.takewhile(lambda x: x < n, psieve()):
        if prime > 2:
            print(',', end='')
        print(prime, end='')
    print('')
test_cases.close()
