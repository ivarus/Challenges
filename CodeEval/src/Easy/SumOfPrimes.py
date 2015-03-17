'''
Created on Feb 11, 2015

@author: Ivan Varus
'''

from math import sqrt

if __name__ == '__main__':
    primes = []
    res = 2
    i = 3
    while True:
        isprime = True
        sqrti = sqrt(i)
        for p in primes:
            if p > sqrti:
                break
            if i % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
            res += i
            if (len(primes) == 999):
                break
        i += 2

    print(res)
