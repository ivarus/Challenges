'''
Created on Mar 17, 2015

@author: Ivan Varus
'''

from collections import deque


def sum_of_digits(_num):
    num = abs(_num)
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res


def accessible(point):
    return sum(map(sum_of_digits, point)) < 20


def walk(start):
    visited = set()
    path = deque()
    path.append(start)
    while len(path) > 0:
        p = path.pop()
        visited.add(p)
        path.extend(filter(lambda pp: accessible(pp) and pp not in visited,
            ((p[0], p[1]-1), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0]+1, p[1]))))
    return len(visited)


if __name__ == '__main__':
    print(walk((0, 0)))
