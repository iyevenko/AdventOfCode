import re
from math import floor, ceil, prod


def num_ways(t, d):
    return ceil(0.5*(t+(t**2-4*d)**0.5)) - floor(0.5*(t-(t**2-4*d)**0.5)) - 1

def solve(f):
    times, distances = open(f).read().splitlines()
    times = map(int, re.findall('\d+', times.split(': ')[1]))
    distances = map(int, re.findall('\d+', distances.split(': ')[1]))
    return prod(num_ways(t, d) for t, d in zip(times, distances))

def solve2(f):
    times, distances = open(f).read().splitlines()
    time = int(''.join(re.findall('\d+', times.split(': ')[1])))
    distance = int(''.join(re.findall('\d+', distances.split(': ')[1])))
    return num_ways(time, distance)

if __name__ == '__main__':
    # print(solve('06_test.txt'))
    print(solve('06.txt'))
    # print(solve2('06_test.txt'))
    print(solve2('06.txt'))
