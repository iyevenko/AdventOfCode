def solve(f):
    coords_str, instructions_str = open(f).read().split('\n\n')
    
    coords = set()
    for s in coords_str.splitlines():
        x, y = s.strip().split(',')
        x, y = int(x), int(y)
        coords.add((x,y))
    
    for instr in instructions_str.splitlines()[:1]:
        new_coords = set()
        if 'y' in instr:
            y_fold = int(instr.strip().split('=')[1])
            for x,y in coords:
                if y > y_fold:
                    new_coords.add((x, 2*y_fold - y))
                else:
                    new_coords.add((x, y))
        else:
            x_fold = int(instr.strip().split('=')[1])
            for x,y in coords:
                if x > x_fold:
                    new_coords.add((2*x_fold - x, y))
                else:
                    new_coords.add((x, y))
        coords = new_coords

    return len(coords)

    
def print_grid(coords):
    xm = min(c[0] for c in coords)
    xM = max(c[0] for c in coords)
    ym = min(c[1] for c in coords)
    yM = max(c[1] for c in coords)

    H = yM - ym + 1
    W = xM - xm + 1
    grid = [[' '] * W for _ in range(H)]

    for x,y in coords:
        grid[y-ym][x-xm] = '█'

    s = ""
    for row in grid:
        s += ''.join(row) + '\n'
    return s


def solve2(f):
    coords_str, instructions_str = open(f).read().split('\n\n')
    
    coords = set()
    for s in coords_str.splitlines():
        x, y = s.strip().split(',')
        x, y = int(x), int(y)
        coords.add((x,y))
    
    for instr in instructions_str.splitlines():
        new_coords = set()
        if 'y' in instr:
            y_fold = int(instr.strip().split('=')[1])
            for x,y in coords:
                if y > y_fold:
                    new_coords.add((x, 2*y_fold - y))
                else:
                    new_coords.add((x, y))
        else:
            x_fold = int(instr.strip().split('=')[1])
            for x,y in coords:
                if x > x_fold:
                    new_coords.add((2*x_fold - x, y))
                else:
                    new_coords.add((x, y))
        coords = new_coords

    return print_grid(coords)
    

if __name__ == '__main__':
    # print(solve('13_test.txt'))
    print(solve('13.txt'))
    # print(solve2('13_test.txt'))
    print(solve2('13.txt'))
