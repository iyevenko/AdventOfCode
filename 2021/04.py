def solve(f):
    chunks = open(f).read().split('\n\n')
    nums = [int(x) for x in chunks[0].strip().split(',')]

    grid_sets = []
    for chunk in chunks[1:]:
        grid = []
        for line in chunk.splitlines():
            grid.append([int(x) for x in line.strip(' \n').split(' ') if x])
        
        rows = [set(r) for r in grid]
        H = W = len(grid)
        cols = [set(r[i] for r in grid) for i in range(H)]
        diags = []
        # diags.append(set(grid[i][i] for i in range(H)))
        # diags.append(set(grid[H-i-1][W-i-1] for i in range(H)))
        grid_sets.append(rows + cols + diags)

    for i in range(5, len(nums)+1):
        nums_subset = set(nums[:i])
        for sets in grid_sets:
            found = False
            for grid_set in sets:
                if grid_set.issubset(nums_subset):
                    found = True
                    break
            if found:
                total = sum(sum(s) for s in sets[:H])
                marked_nums = [x for x in nums_subset if any(x in s for s in sets)]
                return (total - sum(marked_nums)) * nums[i-1]


def solve2(f):
    chunks = open(f).read().split('\n\n')
    nums = [int(x) for x in chunks[0].strip().split(',')]

    grid_sets = []
    for chunk in chunks[1:]:
        grid = []
        for line in chunk.splitlines():
            grid.append([int(x) for x in line.strip(' \n').split(' ') if x])
        
        rows = [set(r) for r in grid]
        H = W = len(grid)
        cols = [set(r[i] for r in grid) for i in range(H)]
        diags = []
        # diags.append(set(grid[i][i] for i in range(H)))
        # diags.append(set(grid[H-i-1][W-i-1] for i in range(H)))
        grid_sets.append(rows + cols + diags)

    for i in range(5, len(nums)+1):
        nums_subset = set(nums[:i])
        remove_inds = []
        for grid_idx, sets in enumerate(grid_sets):
            for grid_set in sets:
                if grid_set.issubset(nums_subset):
                    remove_inds.append(grid_idx)
                    break

        offset = 0
        for grid_idx in remove_inds:
            last_grid = grid_sets.pop(grid_idx - offset)
            offset += 1

        if len(grid_sets) == 0:
            total = sum(sum(s) for s in last_grid[:H])
            marked_nums = [x for x in nums_subset if any(x in s for s in last_grid)]
            return (total - sum(marked_nums)) * nums[i-1]


if __name__ == '__main__':
    # print(solve('04_test.txt'))
    print(solve('04.txt'))
    # print(solve2('04_test.txt'))
    print(solve2('04.txt'))
