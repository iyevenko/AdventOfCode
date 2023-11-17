def print_grid(grid):
    print()
    for row in grid:
        print(''.join(str(x) for x in row))
    print()


def step(grid):
    grid = [[x+1 for x in row] for row in grid]
    flashes = set()
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v > 9:
                flashes.add((i, j))

    flashed = set()
    while flashes:
        flashed |= flashes
        new_flashes = set()
        for i1, j1 in flashes:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    i2, j2 = p = (i1+di, j1+dj)
                    if p == (i1,j1) or p in flashed or not (0 <= i2 <10) or not (0 <= j2 <10):
                        continue
                    grid[i2][j2] += 1
                    if grid[i2][j2] > 9:
                        new_flashes.add(p)
        flashes = new_flashes
    
    for i, j in flashed:
        grid[i][j] = 0

    return grid, len(flashed)


def solve(f, N=100):
    grid = [[0]*10 for _ in range(10)]
    for i, line in enumerate(open(f).read().splitlines()):
        for j, v in enumerate(list(line.strip())):
            grid[i][j] = int(v)
    
    total = 0
    for i in range(N):
        grid, num_flashed = step(grid)
        total += num_flashed
    return total

    
def solve2(f, N=200):
    grid = [[0]*10 for _ in range(10)]
    for i, line in enumerate(open(f).read().splitlines()):
        for j, v in enumerate(list(line.strip())):
            grid[i][j] = int(v)
    
    i = 0
    while True:
        i += 1
        grid, num_flashed = step(grid)
        if num_flashed == 100:
            return i
    

if __name__ == '__main__':
    # print(solve('11_test.txt'))
    print(solve('11.txt'))
    # print(solve2('11_test.txt'))
    print(solve2('11.txt'))
