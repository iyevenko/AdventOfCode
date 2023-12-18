import heapq


def solve(f):
    grid = {}
    lines = open(f).read().splitlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[(i,j)] = int(c)

    M, N = len(lines), len(lines[0])
    ## Dijkstra
    q = [(0, 0, 0, (0,0), [(0,0)])]
    best = 1e9
    g = {}
    while q:
        d2s, i, j, last_n, history = heapq.heappop(q)
        num_i, num_j = last_n
        
        if (i,j) == (M-1, N-1):
            best = min(best, d2s)
            continue
        # last_n must be included in the state
        key = (i, j, last_n)
        if g.get(key, 1e9) <= d2s or d2s >= best:
            continue
        g[key] = d2s

        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i+di, j+dj
            if (ni, nj) not in grid:
                continue
            if len(history) > 1 and (ni, nj) == history[-2]:
                continue

            new_last_n = last_n
            new_last_n = (num_i+1, 0) if ni == i else (0, num_j+1)
            if 3+1 in new_last_n:
                continue
            
            heapq.heappush(q, (d2s + grid[(ni, nj)], ni, nj, new_last_n, history[-1:]+[(ni,nj)]))

    return best


def solve2(f):
    grid = {}
    lines = open(f).read().splitlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[(i,j)] = int(c)

    M, N = len(lines), len(lines[0])
    ## Dijkstra
    q = [(0, 0, 0, (0,0), [(0,0)])]
    best = 1e9
    g = {}
    while q:
        d2s, i, j, last_n, history = heapq.heappop(q)
        num_i, num_j = last_n
        
        if (i,j) == (M-1, N-1) and (num_i >= 4 or num_j >= 4):
            best = min(best, d2s)
            continue
        # last_n must be included in the state
        key = (i, j, last_n)
        if g.get(key, 1e9) <= d2s or d2s >= best:
            continue
        g[key] = d2s

        if (i,j) == (0,0):
            deltas = [(1,0),(0,1)]
        else:
            last_di, last_dj = (i-history[-2][0],j-history[-2][1])
            if not (num_i >= 4 or num_j >= 4):
                deltas = [(last_di,last_dj)]
            else:
                deltas = [(0,1),(1,0),(0,-1),(-1,0)]
                deltas.remove((-last_di,-last_dj))

        for di, dj in deltas:
            ni, nj = i+di, j+dj
            if (ni, nj) not in grid:
                continue

            new_last_n = (num_i+1, 0) if ni == i else (0, num_j+1)
            if 10+1 in new_last_n:
                continue
            
            heapq.heappush(q, (d2s + grid[(ni, nj)], ni, nj, new_last_n, history[-1:]+[(ni,nj)]))

    return best


if __name__ == '__main__':
    # print(solve('17_test.txt'))
    print(solve('17.txt'))
    # print(solve2('17_test.txt'))
    # print(solve2('17_test2.txt'))
    print(solve2('17.txt'))
