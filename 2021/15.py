import heapq


def bfs(grid):
    H, W = len(grid), len(grid[0])

    dp = [[1e9]*W for _ in range(H)]
    q = []
    heapq.heappush(q, (0,0,0))
    while q:
        risk, i, j = heapq.heappop(q)
        for i2, j2 in [(i,j+1), (i+1,j), (i,j-1), (i-1,j)]:
            if not (0 <= i2 < W and 0 <= j2 < H):
                continue
            new_risk = risk + grid[i2][j2]
            if new_risk < dp[i2][j2]:
                dp[i2][j2] = new_risk
                heapq.heappush(q, (new_risk, i2, j2))

    return dp[H-1][W-1]


def solve(f):
    grid = []
    for line in open(f).read().splitlines():
        grid.append([int(x) for x in line.strip()])
    
    return bfs(grid)

def solve2(f):
    grid = []
    for line in open(f).read().splitlines():
        grid.append([int(x) for x in line.strip()])

    big_grid = []
    for i in range(5):
        for row in grid:
            new_row = []
            for j in range(5):
                new_row.extend([x+i+j if x+i+j < 10 else (x+i+j) % 10 + 1 for x in row])
            big_grid.append(new_row)
    
    return bfs(big_grid)
    

if __name__ == '__main__':
    # print(solve('15_test.txt'))
    print(solve('15.txt'))
    # print(solve2('15_test.txt'))
    print(solve2('15.txt'))
