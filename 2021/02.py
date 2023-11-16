from collections import deque


def solve(f):
    h = 0
    v = 0
    for instr in open(f).read().splitlines():
        d, n = instr.split(' ')
        n = int(n)
        if d == 'forward':
            h += n
        elif d == 'down':
            v += n
        elif d == 'up':
            v -= n
    return v * h


def solve2(f):
    h = 0
    v = 0
    aim = 0
    for instr in open(f).read().splitlines():
        d, n = instr.split(' ')
        n = int(n)
        if d == 'forward':
            h += n
            v += aim * n
        elif d == 'down':
            aim += n
        elif d == 'up':
            aim -= n
    return v * h

if __name__ == '__main__':
    # print(solve('02_test.txt'))
    print(solve('02.txt'))
    # print(solve2('02_test.txt'))
    print(solve2('02.txt'))