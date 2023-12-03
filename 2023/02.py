def solve(f):
    total = 0
    for i, line in enumerate(open(f).read().splitlines()):
        _, s = line.split(': ')
        good = True
        for set in s.split('; '):
            colors = {}
            for x, c in map(lambda x: x.split(' '), set.split(', ')):
                colors[c] = int(x)
            if colors.get('red', 0) > 12 or colors.get('green', 0) > 13 or colors.get('blue', 0) > 14:
                good = False
                break
        if good:
            total += i + 1
    return total


def solve2(f):
    total = 0
    for line in open(f).read().splitlines():
        s = ' '.join(line.split(' ')[2:])
        colors = {}
        for set in s.split('; '):
            for x, c in map(lambda x: x.split(' '), set.split(', ')):
                colors[c] = max(colors.get(c, 0), int(x))
        total += colors.get('red', 0) * colors('green', 0) * colors.get('blue', 0)
    return total
    

if __name__ == '__main__':
    # print(solve('02_test.txt'))
    print(solve('02.txt'))
    # print(solve2('02_test.txt'))
    print(solve2('02.txt'))
