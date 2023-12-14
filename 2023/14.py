def rotate(n, grid):
    n %= 4
    if n == 0:
        return grid
    for _ in range(n):
        grid = [''.join(row) for row in zip(*grid[::-1])]
    return grid

def calculate_load(grid):
    load = 0
    for i, row in enumerate(grid):
        load += (len(grid)-i) * row.count('O')
    return load

def tilt_grid(grid, direction):
    dirs = {'N':-1, 'W':0, 'E':1, 'S':2}
    grid = rotate(dirs[direction], grid)
    new_grid = []
    for row in grid:
        last_cube = -1
        last_round = -1
        i = 0
        new_row = ['.'] * len(row)
        while i < len(row):
            if row[i] == '.':
                i+= 1
                continue
            if row[i] == '#':
                last_cube = i
                last_round = i
                new_row[i] = '#'
                i += 1
                continue
            new_pos = max(last_cube+1, last_round+1)
            last_round = new_pos
            new_row[new_pos] = 'O'
            i += 1
        new_grid.append(''.join(new_row))
    return rotate(-dirs[direction], new_grid)

def solve(f):
    grid = open(f).read().splitlines()
    grid = tilt_grid(grid, 'N')
    return calculate_load(grid)

def solve2(f):
    grid = open(f).read().splitlines()
    loads = {}
    for i in range(1000):
        for direction in ['N', 'W', 'E', 'S']:
            grid = tilt_grid(grid, direction)
        load = calculate_load(grid)

        grid_key = ''.join(grid)
        if grid_key in loads:
            load, idx = loads[grid_key]
            offset, modulo = idx, i+1-idx
            break
        loads[grid_key] = (load, i+1)

    for load, idx in loads.values():
        if idx == (1000000000-offset)%modulo + offset:
            return load


if __name__ == '__main__':
    # print(solve('14_test.txt'))
    print(solve('14.txt'))
    # print(solve2('14_test.txt'))
    print(solve2('14.txt'))
