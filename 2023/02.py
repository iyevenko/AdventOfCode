def solve(f):
    total = 0
    for i, line in enumerate(open(f).read().splitlines()):
        _, s = line.split(': ')
        possible = True
        for set in s.split('; '):
            colors = {color: int(x) for x, color in [pair.split(' ') for pair in set.split(', ')]}
            if colors.get('red', 0) > 12 or colors.get('green', 0) > 13 or colors.get('blue', 0) > 14:
                possible = False
                break
        if possible:
            total += i + 1
    return total


def solve2(f):
    total = 0
    for line in open(f).read().splitlines():
        _, s = line.split(': ')
        colors = {}
        for set in s.split('; '):
            for x, color in [pair.split(' ') for pair in set.split(', ')]:
                colors[color] = max(colors.get(color, 0), int(x))
        total += colors.get('red', 0) * colors.get('green', 0) * colors.get('blue', 0)
    return total
    

if __name__ == '__main__':
    # print(solve('02_test.txt'))
    print(solve('02.txt'))
    # print(solve2('02_test.txt'))
    print(solve2('02.txt'))
