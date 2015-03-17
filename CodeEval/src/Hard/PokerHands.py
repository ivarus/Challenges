'''
Created on Mar 10, 2015

@author: Ivan Varus
'''

import sys
from collections import Counter
from operator import itemgetter


rankings = {
    (4, 1): 7,
    (3, 2): 6,
    # 5 for flush
    # 4 for straight
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0
}


def score(hand):
    c = Counter('0123456789TJQKA'.index(card[0]) for card in hand)
    # Unfortunately, we can't use just c.most_common(), because
    # most_common() returns elements with equal counts in arbitrary order
    ranks, counts = zip(*sorted(c.items(), key=itemgetter(1, 0), reverse=True))
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and ranks[0] - ranks[4] == 4
    flush = len(set(card[1] for card in hand)) == 1
    # return combination ranking, which will be compared first, and if two
    # hands are equal, card ranks will be compared after in appropriate order
    return max(rankings[counts], 4*straight + 5*flush), ranks


def cmp(a, b):
    return (a > b) - (a < b)


def compare(*args):
    return ['none', 'left', 'right'][cmp(*map(score, args))]


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        ls = test.split()
        print(compare(ls[:5], ls[5:]))
