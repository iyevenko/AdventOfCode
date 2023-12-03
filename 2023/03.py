def solve(f):
    symbols = set()
    part_numbers = []
    for i, line in enumerate(open(f).read().splitlines()):
        q = []
        for j, c in enumerate(line):
            if c == '.' and not q:
                continue
            elif c == '.':
                part_number = "".join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []
            elif c.isnumeric():
                q.append(c)
            else:
                symbols.add((i,j))
                part_number = "".join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []
        if q:
            part_number = "".join(q)
            part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))

    s = 0
    for part_number, coords in part_numbers:
        found = False
        for (i,j) in coords:
            for _i in range(i-1, i+2):
                for _j in range(j-1, j+2):
                    if (_i,_j) in symbols:
                        s += int(part_number)
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return s

def solve2(f):
    symbols = {}
    part_numbers = []
    for i, line in enumerate(open(f).read().splitlines()):
        q = []
        for j, c in enumerate(line):
            if c == '.' and not q:
                continue
            elif c == '.':
                part_number = "".join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []
            elif c.isnumeric():
                q.append(c)
            else:
                symbols[(i,j)] = c
                part_number = "".join(q)
                part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))
                q = []
        if q:
            part_number = "".join(q)
            part_numbers.append((part_number, [(i, k) for k in range(j - len(part_number), j)]))

    gears = {}
    for part_number, coords in part_numbers:
        found = False
        for (i,j) in coords:
            for _i in range(i-1, i+2):
                for _j in range(j-1, j+2):
                    if (_i,_j) in symbols and symbols[(_i,_j)] == '*':
                        gears[(_i,_j)] = gears.get((_i,_j), []) + [part_number]
                        found = True
                        break
                if found:
                    break
            if found:
                break

    s = 0
    for gear, part_numbers in gears.items():
        if len(part_numbers) == 2:
            s += int(part_numbers[0]) * int(part_numbers[1])
    return s
    

if __name__ == '__main__':
    print(solve('03_test.txt'))
    print(solve('03.txt'))
    print(solve2('03_test.txt'))
    print(solve2('03.txt'))
