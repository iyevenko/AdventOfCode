reflections = {
    '|': {
        (0, 1): [(1, 0),(-1, 0)],
        (0, -1): [(1, 0),(-1, 0)],
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
    },
    '-': {
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
        (1, 0): [(0, -1),(0, 1)],
        (-1, 0): [(0, -1),(0, 1)]
    },
    '/': {
        (0, 1): [(-1, 0)],
        (0, -1): [(1, 0)],
        (1, 0): [(0, -1)],
        (-1, 0): [(0, 1)],
    },
    '\\': {
        (0, 1): [(1, 0)],
        (0, -1): [(-1, 0)],
        (1, 0): [(0, 1)],
        (-1, 0): [(0, -1)],
    },
    '.': {
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
    },
}


def num_energized(edges, start, dir):
    q = [(start, dir)]
    visited = set()
    points = set()
    while q:
        (i, j), (di, dj) = q.pop(0)
        ni, nj = i+di, j+dj
        c = edges.get((ni, nj), None)
        if c in reflections:
            for ndi, ndj in reflections[c][(di, dj)]:
                k = (ni,nj,ndi,ndj)
                if k in visited:
                    continue
                visited.add(k)
                points.add((ni,nj))
                q.append(((ni, nj), (ndi, ndj)))
    return len(points)


def solve(f):
    edges = {}
    for i, line in enumerate(open(f).read().splitlines()):
        for j, c in enumerate(line):
            edges[(i,j)] = c

    return num_energized(edges, (0,-1), (0,1))


def solve2(f):
    edges = {}
    lines = open(f).read().splitlines()
    N, M = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            edges[(i,j)] = c

    best = 0
    for r in range(N):
        best = max(best, num_energized(edges, (r,-1), (0,1)))
        best = max(best, num_energized(edges, (r,M), (0,-1)))
    for c in range(M):
        best = max(best, num_energized(edges, (-1,c), (1,0)))
        best = max(best, num_energized(edges, (N,c), (-1,0)))
    return best


if __name__ == '__main__':
    # print(solve('16_test.txt'))
    print(solve('16.txt'))
    # print(solve2('16_test.txt'))
    print(solve2('16.txt'))
