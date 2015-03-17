'''
Created on Mar 17, 2015

@author: Ivan Varus
'''


def sum_of_digits(_num):
    num = abs(_num)
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res


def accessible(p):
    return sum(map(sum_of_digits, p)) < 20


def walk(start):
    visited = set()
    # its very interesting, but tests show that a set with pop()
    # arbitrary element will perform much faster, than deque
    path = set()
    path.add(start)
    while len(path) > 0:
        p = path.pop()
        visited.add(p)
        path.update(filter(lambda pp: pp not in visited and accessible(pp),
            ((p[0], p[1]-1), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0]+1, p[1]))))
    return len(visited)


if __name__ == '__main__':
    print(walk((0, 0)))
