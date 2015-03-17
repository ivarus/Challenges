'''
Created on Feb 10, 2015

@author: Ivan Varus
'''


def dectovec(dec_n):
    vec = []
    p = 0
    while True:
        rank = 10 ** p
        if dec_n < rank:
            break
        n = (dec_n // rank) % 10
        vec.append(n)
        p += 1
    return vec


if __name__ == '__main__':
    primes = [2]
    for i in range(3, 1000):
        isprime = True
        for p in primes:
            if i % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
    for i in range(len(primes)-1, -1, -1):
        v = dectovec(primes[i])
        ispalindrome = True
        for j in range(0, len(v) // 2):
            if v[j] != v[len(v)-1-j]:
                ispalindrome = False
                break
        if ispalindrome:
            print(primes[i])
            break
