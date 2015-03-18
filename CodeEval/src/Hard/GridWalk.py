'''
Created on Mar 17, 2015

@author: Ivan Varus

'''


# will return maximum coordinate (x or y) which monkey can reach
# for given sum of digits.
def longest_path(sod):
    path = [9] * (sod // 9) + [sod % 9]
    return sum(x * 10 ** p for p, x in enumerate(path))


def sum_of_digits(num):
    n = abs(num)
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def accessible(p):
    return sum(map(sum_of_digits, p)) < 20


def walk(start):
    # its very interesting, but tests show, that if we make a set
    # which we will be checking for visited points will perform faster
    # or at least as fast as checking in a state matrix by indexes
    # as points with constant lookup speed
    visited = set()
    # its very interesting again, but tests show that a set with pop()
    # arbitrary element will perform much faster, than deque
    path = set()
    path.add(start)
    while len(path) > 0:
        p = path.pop()
        visited.add(p)
        path.update(filter(lambda pp:  pp not in visited and min(*pp) >= 0 and
                           accessible(pp), ((p[0], p[1]-1), (p[0], p[1]+1),
                                            (p[0]-1, p[1]), (p[0]+1, p[1]))))
    max_len = longest_path(20)
    # 4 times quadrant minus 4 overlapping axes and add center point
    return len(visited) * 4 - 4 * max_len + 1


if __name__ == '__main__':
    print(walk((0, 0)))
