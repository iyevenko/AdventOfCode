def iter_neighbors(i, j, m=None, n=None, diagonal=True, include_center=False):
    # Used in a lot of AoC problems
    if m is None:
        m = i + 2
    if n is None:
        n = j + 2

    if include_center and 0 <= i < m and 0 <= j < n:
        yield (i,j)
    
    if not diagonal:
        for _i, _j in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if 0 <= _i < m and 0 <= _j < n:
                yield (_i, _j)
    else:
        for _i in range(max(0, i-1), min(m, i+2)):
            for _j in range(max(0, j-1), min(n, j+2)):
                if (_i,_j) != (i,j):
                    yield (_i,_j)


def solve(f):
    symbols = set()
    part_numbers = []
    for i, line in enumerate(open(f).read().splitlines()):
        q = []
        for j, c in enumerate(line + '.'):
            if c == '.' and not q:
                continue
            if c.isnumeric():
                q.append(c)
            else:
                if c != '.':
                    symbols.add((i,j))
                part_number = ''.join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []

    s = 0
    for part_number, coords in part_numbers:
        found = False
        for (i,j) in coords:
            for _i, _j in iter_neighbors(i, j, diagonal=True):
                if (_i,_j) in symbols:
                    s += int(part_number)
                    found = True
                    break
            if found:
                break
    return s

def solve2(f):
    symbols = {}
    part_numbers = []
    for i, line in enumerate(open(f).read().splitlines()):
        q = []
        for j, c in enumerate(line + '.'):
            if c == '.' and not q:
                continue
            if c.isnumeric():
                q.append(c)
            else:
                if c != '.':
                    symbols[(i,j)] = c
                part_number = ''.join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []

    gears = {}
    for part_number, coords in part_numbers:
        found = False
        for (i,j) in coords:
            for _i, _j in iter_neighbors(i, j, diagonal=True):
                if (_i,_j) in symbols and symbols[(_i,_j)] == '*':
                    gears[(_i,_j)] = gears.get((_i,_j), []) + [part_number]
                    found = True
                    break
            if found:
                break

    s = 0
    for part_numbers in gears.values():
        if len(part_numbers) == 2:
            s += int(part_numbers[0]) * int(part_numbers[1])
    return s
    

if __name__ == '__main__':
    # print(solve('03_test.txt'))
    print(solve('03.txt'))
    # print(solve2('03_test.txt'))
    print(solve2('03.txt'))
