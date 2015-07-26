from sys import argv


def get_arrow_count(s):
    return sum(
        s[i:i+5] in ('>>-->', '<--<<')
        for i in range(len(s)-4)
    )


with open(argv[1], 'r') as tests:
    for t in tests:
        print(get_arrow_count(t.rstrip()))
