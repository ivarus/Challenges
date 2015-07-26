from sys import argv

with open(argv[1]) as tests:
    for t in tests:
        ls = sorted(map(int, t.split()[1:]))
        solution = ls[len(ls) // 2]
        print(sum(abs(solution - e) for e in ls))
