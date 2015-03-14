'''
Created on Mar 14, 2015

@author: Ivan Varus

Thanks: Ferhat Elmas
'''


visited = [[False]*4 for _ in range(4)]


def step(i, j):
    if i == 3 and j == 3:
        return 1
    if min(i, j) < 0 or max(i, j) > 3:
        return 0
    if visited[i][j]:
        return 0
    visited[i][j] = True
    count = step(i, j-1) + step(i, j+1) + step(i-1, j) + step(i+1, j)
    visited[i][j] = False
    return count


def robotMovements():
    return step(0, 0)


if __name__ == '__main__':
    print(robotMovements())
