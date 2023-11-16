def solve(f):
    points = set()
    interection_points = set()
    for line in open(f).read().splitlines():
        start, end = line.strip().split(' -> ')
        x1, y1 = [int(x) for x in start.split(',')]
        x2, y2 = [int(x) for x in end.split(',')]

        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2+1):
                p = (x1, y)
                if p in points and p not in interection_points:
                    interection_points.add(p)
                else:
                    points.add(p)
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2+1):
                p = (x, y1)
                if p in points and p not in interection_points:
                    interection_points.add(p)
                else:
                    points.add(p)
    return len(interection_points)


def solve2(f):
    points = set()
    interection_points = set()
    for line in open(f).read().splitlines():
        start, end = line.strip().split(' -> ')
        x1, y1 = [int(x) for x in start.split(',')]
        x2, y2 = [int(x) for x in end.split(',')]


        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2+1):
                p = (x1, y)
                if p in points and p not in interection_points:
                    interection_points.add(p)
                else:
                    points.add(p)
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2+1):
                p = (x, y1)
                if p in points and p not in interection_points:
                    interection_points.add(p)
                else:
                    points.add(p)
        elif abs(x2-x1) == abs(y2-y1):
            if x2 > x1:
                x_range = range(x1, x2+1)
            else:
                x_range = reversed(range(x2, x1+1))
            if y2 > y1:
                y_range = range(y1, y2+1)
            else:
                y_range = reversed(range(y2, y1+1))
            
            for x, y in zip(x_range, y_range):
                p = (x, y)
                if p in points and p not in interection_points:
                    interection_points.add(p)
                else:
                    points.add(p)



    return len(interection_points)
    

if __name__ == '__main__':
    # print(solve('05_test.txt'))
    # print(solve('05.txt'))
    # print(solve2('05_test.txt'))
    print(solve2('05.txt'))
