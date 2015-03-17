'''
Created on Mar 11, 2015

@author: Ivan Varus
'''

import sys
from itertools import *


def build_keymap(header):
    it = iter(header)
    keymap = list(takewhile(lambda ls: len(ls) > 0,
                            (list(islice(it, 2**i-1)) for i in count(1))))
    return keymap


def take_segment(message, size):
    return ''.join(islice(message, size))


def decode(header, message):
    keymap = build_keymap(header)
    while True:
        keysize = int(take_segment(message, 3), 2)
        if keysize == 0:
            break
        while True:
            key = take_segment(message, keysize)
            if '0' not in key:
                break
            yield keymap[keysize-1][int(key, 2)]


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        isheader = lambda c: c not in '01'
        print(''.join(decode(takewhile(isheader, test),
                             dropwhile(isheader, test))))
