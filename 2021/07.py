def solve(f):
    crabs = sorted(map(int, open(f).read().strip().split(',')))

    def distance(pos):
        return sum(abs(x-pos) for x in crabs)

    mid = crabs[len(crabs)//2]
    d = distance(mid)
    while True:
        dl = distance(mid-1)
        dr = distance(mid+1)
        if dl < d:
            mid -= 1
            d = dl
        elif dr < d:
            mid += 1
            d = dr
        else:
            return d


def solve2(f):
    crabs = sorted(map(int, open(f).read().strip().split(',')))

    def g(x):
        return x*(x+1)//2

    def distance(pos):
        return sum(g(abs(x-pos)) for x in crabs)
    
    mid = crabs[len(crabs)//2]
    d = distance(mid)
    while True:
        dl = distance(mid-1)
        dr = distance(mid+1)
        if dl < d:
            mid -= 1
            d = dl
        elif dr < d:
            mid += 1
            d = dr
        else:
            return d
    

if __name__ == '__main__':
    # print(solve('07_test.txt'))
    print(solve('07.txt'))
    # print(solve2('07_test.txt'))
    print(solve2('07.txt'))
