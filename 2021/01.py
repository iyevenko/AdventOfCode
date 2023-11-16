from collections import deque


def solve(f):
    j = 1e9
    count = 0
    for i in map(int, open(f).read().splitlines()):
        if i > j:
            count += 1
        j = i
    return count

def solve2(f):
    q = deque(maxlen=3)
    count = 0
    for i in map(int, open(f).read().splitlines()):
        if len(q) < 3:
            q.append(i)
            continue
        s1 = sum(q)
        q.append(i)
        s2 = sum(q)
        if s2 > s1:
            count += 1
    return count
    

if __name__ == '__main__':
    # print(solve('01_test.txt'))
    print(solve('01.txt'))
    # print(solve2('01_test.txt'))
    print(solve2('01.txt'))