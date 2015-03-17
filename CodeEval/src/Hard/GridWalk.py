'''
Created on Mar 17, 2015

@author: Ivan Varus

'''


def sum_of_digits(num):
    n = abs(num)
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def accessible(p):
    # reduce area to only one quadrant
    return min(p[0], p[1]) >= 0 and sum(map(sum_of_digits, p)) < 20


# will return maximum coordinate (x or y) which monkey can reach
# for given sum of digits
def longest_path(sod):
    n = sod
    path = []
    while n > 9:
        n -= 9
        path.append(9)
    path.append(n)
    ret = 0
    p = 0
    for x in path:
        ret += x * 10 ** p
        p += 1
    return ret


def walk(start):
    visited = set()
    # its very interesting, but tests show that a set with pop()
    # arbitrary element will perform much faster, than deque
    path = set()
    path.add(start)
    max_coord = longest_path(20)
    while len(path) > 0:
        p = path.pop()
        visited.add(p)
        path.update(filter(lambda pp: pp not in visited and accessible(pp),
            ((p[0], p[1]-1), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0]+1, p[1]))))
    # 4 times quadrant minus 4 overlapping axes and add center point
    return len(visited) * 4 - 4 * max_coord + 1


if __name__ == '__main__':
    print(walk((0, 0)))
