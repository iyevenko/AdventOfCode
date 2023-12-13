def find_line(grid):
    lines = grid.splitlines()
    M = len(lines)
    N = len(lines[0])

    possible = set(range(1,N))
    for i in range(M):
        row = lines[i]
        for j in list(possible):
            w = min(N-j, j)
            if row[j-w:j] != row[j+w-1:j-1:-1]:
                possible.discard(j)
            if not possible:
                break
    
    if possible:
        return possible.pop(), 0
    
    possible = set(range(1,M))
    for j in range(N):
        col = ''.join(line[j] for line in lines)
        for i in list(possible):
            w = min(M-i, i)
            if col[i-w:i] != col[i+w-1:i-1:-1]:
                possible.discard(i)
            if not possible:
                break
    return 0, possible.pop()

        
def find_line2(grid):
    lines = grid.splitlines()
    M = len(lines)
    N = len(lines[0])
    counts = {k: 0 for k in range(1,N)}
    for i in range(M):
        row = lines[i]
        for j in range(1, N):
            w = min(N-j, j)
            if row[j-w:j] == row[j+w-1:j-1:-1]:
                counts[j] += 1

    for k, v in counts.items():
        if v == M-1:
            return k, 0
    
    counts = {k: 0 for k in range(1,M)}
    for j in range(N):
        col = ''.join(line[j] for line in lines)
        for i in range(1, M):
            w = min(M-i, i)
            if col[i-w:i] == col[i+w-1:i-1:-1]:
                counts[i] += 1

    for k, v in counts.items():
        if v == N-1:
            return 0, k

    return 0,0


def solve(f):
    s = 0
    grids = open(f).read().split('\n\n')
    for grid in grids:
        c, r = find_line(grid)
        s += c + 100*r
    return s
        

def solve2(f):
    s = 0
    grids = open(f).read().split('\n\n')
    for grid in grids:
        c, r = find_line2(grid)
        s += c + 100*r
    return s
    

if __name__ == '__main__':
    # print(solve('13_test.txt'))
    print(solve('13.txt'))
    # print(solve2('13_test.txt'))
    print(solve2('13.txt'))
