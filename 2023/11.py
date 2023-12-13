def solve_general(f, multiplier):
    points = []
    lines = open(f).read().splitlines()
    for i, line in enumerate(lines):
        points.extend([(i, j) for j, c in enumerate(line) if c != '.'])
    
    N, M = len(lines), len(lines[0])
    expand_rows = set(i for i in range(N) if not any(p[0] == i for p in points))
    expand_cols = set(j for j in range(M) if not any(p[1] == j for p in points))

    distances = 0
    for j, (pi, pj) in enumerate(points):
        for oi, oj in points[j+1:]:
            if pi == oi and pj == oj:
                continue
            di = abs(pi - oi) + (multiplier-1) * len(set(range(min(pi, oi) + 1, max(pi, oi))) & expand_rows)
            dj = abs(pj - oj) + (multiplier-1) * len(set(range(min(pj, oj) + 1, max(pj, oj))) & expand_cols)
            distances += di + dj
    return distances

def solve(f):
    return solve_general(f, 2)

def solve2(f):
    return solve_general(f, 1000000)
    

if __name__ == '__main__':
    # print(solve('11_test.txt'))
    print(solve('11.txt'))
    # print(solve2('11_test.txt'))
    print(solve2('11.txt'))
