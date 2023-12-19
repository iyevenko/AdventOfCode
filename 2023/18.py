def solve(f):
    curr = (0,0)
    points = {curr}
    for line in open(f).read().splitlines():
        r, n, _ = line.split(' ')
        n = int(n)
        if r == 'R':
            for i in range(n):
                points.add((curr[0], curr[1]+i+1))
            curr = (curr[0], curr[1]+n)
        elif r == 'L':
            for i in range(n):
                points.add((curr[0], curr[1]-i-1))
            curr = (curr[0], curr[1]-n)
        elif r == 'D':
            for i in range(n):
                points.add((curr[0]+i+1, curr[1]))
            curr = (curr[0]+n, curr[1])
        elif r == 'U':
            for i in range(n):
                points.add((curr[0]-i-1, curr[1]))
            curr = (curr[0]-n, curr[1])

    # flood fill
    curr = (1,1)
    q = [curr]
    while q:
        i, j = q.pop(0)
        for next in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if next in points:
                continue
            points.add(next)
            q.append(next)
    return len(points)


def solve2(f):
    curr = (0,0)
    horiz = {}
    vert = {}
    A = 0
    for line in open(f).read().splitlines():
        _, _, c = line.split(' ')
        n = int(c[2:7], base=16)
        r = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[c[7]]
        i, j = curr
        A += n
        if r == 'R':
            curr = (i, j+n)
            horiz[i] = horiz.get(i, [])
            horiz[i].append((j, j+n))
        elif r == 'L':
            curr = (i, j-n)
            horiz[i] = horiz.get(i, [])
            horiz[i].append((j-n, j))
        elif r == 'D':
            curr = (i+n, j)
            vert[j] = vert.get(j, [])
            vert[j].append((i, i+n))
        elif r == 'U':
            curr = (i-n, j)
            vert[j] = vert.get(j, [])
            vert[j].append((i-n, i))

    for i in horiz:
        horiz[i].sort()

    for j in vert:
        vert[j].sort()

    rows = sorted(horiz.keys())
    cols = sorted(vert.keys())

    def in_ranges(x, ranges):
        return any(lo <= x <= hi for lo, hi in ranges)
    
    # precompute num_above (optimization)
    num_above = []
    for i in range(len(rows)-1):
        r = rows[i]
        num_above.append([0] * (len(cols)-1))
        for j in range(len(cols)-1):
            c = cols[j]
            prev = num_above[i-1][j] if i > 0 else 0
            num_above[i][j] = int(in_ranges(c+0.5, horiz[r])) + prev

    for i in range(len(rows)-1):
        r1, r2 = rows[i:i+2]
        for j in range(len(cols)-1):
            c1, c2 = cols[j:j+2]
            add_right = not in_ranges(r1+0.5, vert[c2])
            add_below = not in_ranges(c1+0.5, horiz[r2])
            add_corner = not (in_ranges(c2, horiz[r2]) or in_ranges(r2, vert[c2]))
            if (num_above[i][j]%2 == 1):
                dA = (r2-r1-1)*(c2-c1-1) # 2D area
                if add_right:
                    dA += (r2-r1-1) # 1D area
                if add_below:
                    dA += (c2-c1-1) # 1D area
                if add_corner:
                    dA += 1 # 0D area
                A += dA
    return A

if __name__ == '__main__':
    # print(solve('18_test.txt'))
    print(solve('18.txt'))
    # print(solve2('18_test.txt'))
    print(solve2('18.txt'))