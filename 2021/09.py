from math import prod

def solve(f):
    grid = []
    for line in open(f).read().splitlines():
        grid.append(list(map(int, list(line))))

    H = len(grid)
    W = len(grid[0])
    padded_grid = [[10] * (W+2)]
    for row in grid:
        padded_grid.append([10] + row + [10])
    padded_grid.append([10] * (W+2))

    grid = padded_grid

    low = []
    for i in range(1, H+1):
        for j in range(1, W+1):
            v = grid[i][j]
            if v < grid[i-1][j] and v < grid[i+1][j] and v < grid[i][j-1] and v < grid[i][j+1]:
                low.append(v)

    return sum(x+1 for x in low)


def expand_basin(grid, outer_points, points):
    if not outer_points:
        return points

    new_points = set()
    for i, j in outer_points:
        for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            p = (new_i, new_j)
            if p in points or grid[new_i][new_j] >= 9:
                continue
            new_points.add(p)

    return expand_basin(grid, new_points, points | outer_points)

def solve2(f):
    grid = []
    for line in open(f).read().splitlines():
        grid.append(list(map(int, list(line))))

    H = len(grid)
    W = len(grid[0])
    padded_grid = [[10] * (W+2)]
    for row in grid:
        padded_grid.append([10] + row + [10])
    padded_grid.append([10] * (W+2))

    grid = padded_grid

    low = []
    for i in range(1, H+1):
        for j in range(1, W+1):
            v = grid[i][j]
            if v < grid[i-1][j] and v < grid[i+1][j] and v < grid[i][j-1] and v < grid[i][j+1]:
                low.append((i, j))

    basin_sizes = []
    for low_point in low:
        basin = expand_basin(grid, {low_point}, set())
        basin_sizes.append(len(basin))
    return prod(sorted(basin_sizes, reverse=True)[:3])
    

if __name__ == '__main__':
    # print(solve('09_test.txt'))
    print(solve('09.txt'))
    # print(solve2('09_test.txt'))
    print(solve2('09.txt'))
