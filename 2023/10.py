PIPES = {
    '|': [(-1 ,0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
}

def detect_loop(graph, start):
    queue = [start]
    visited = {start}
    depth = -1
    while queue:
        depth += 1
        new_queue = []
        for i, j in queue:
            for di, dj in graph[(i, j)]:
                ni, nj = i + di, j + dj
                if (ni, nj) in visited or (ni, nj) not in graph:
                    continue
                neg = (-di, -dj)
                if neg not in graph[(ni, nj)]:
                    continue
                visited.add((ni, nj))
                new_queue.append((ni, nj))
        queue = new_queue
    return visited, depth


def solve(f):
    graph = {}
    start = None
    for i, line in enumerate(open(f).read().splitlines()):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                graph[start] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            elif c != '.':
                graph[(i, j)] = PIPES[c]

    _, depth = detect_loop(graph, start)
    return depth


def solve2(f):
    graph = {}
    start = None
    empty = set()
    pipe_points = {}
    lines = open(f).read().splitlines()
    N, M = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                graph[start] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                pipe_points[(i, j)] = c
            elif c == '.':
                empty.add((i, j))
            else:
                graph[(i, j)] = PIPES[c]
                pipe_points[(i, j)] = c

    loop, _ = detect_loop(graph, start)
    
    inside_points = set()
    for i in range(N):
        inside_loop = False
        pipe_start = None
        for j in range(M):
            if (i, j) in loop:
                c = pipe_points[(i, j)]
                if c == '|':
                    inside_loop = not inside_loop
                elif c in 'LF':
                    pipe_start = c
                elif (c == 'J' and pipe_start in 'SF') or (c == '7' and pipe_start in 'SL'):
                    inside_loop = not inside_loop
                    pipe_start = None
                elif c == 'S':
                    inside_loop = not inside_loop
                    pipe_start = 'S'
            elif inside_loop:
                inside_points.add((i, j))
    
    ## DEBUG
    # grid = ""
    # for i in range(N):
    #     for j in range(M):
    #         grid += pipe_points[(i, j)] if (i, j) in loop else 'X' if (i, j) in inside_points else '.' if (i, j) in empty else ' '
    #     grid += '\n'
    # print(grid)
    # print()

    return len(inside_points)
    

if __name__ == '__main__':
    # print(solve('10_test.txt'))
    print(solve('10.txt'))
    # print(solve2('10_test2.txt'))
    # print(solve2('10_test3.txt'))
    print(solve2('10.txt'))
