def extrapolate(nums):
    q = nums
    last_vals = [q[-1]]
    while any(q):
        q = [y-x for x, y in zip(q[:-1], q[1:])]
        last_vals.append(q[-1])
    last_vals.pop()

    ret = 0
    while last_vals:
        ret += last_vals.pop()
    return ret

def extrapolate_back(nums):
    q = nums
    last_vals = [q[0]]
    while any(q):
        q = [y-x for x, y in zip(q[:-1], q[1:])]
        last_vals.append(q[0])
    last_vals.pop()

    ret = 0
    while last_vals:
        ret = last_vals.pop() - ret
    return ret

def solve(f):
    s = 0
    for line in open(f).read().splitlines():
        s += extrapolate([int(x) for x in line.split(' ')])
    return s

def solve2(f):
    s = 0
    for line in open(f).read().splitlines():
        s += extrapolate_back([int(x) for x in line.split(' ')])
    return s
    

if __name__ == '__main__':
    # print(solve('09_test.txt'))
    print(solve('09.txt'))
    # print(solve2('09_test.txt'))
    print(solve2('09.txt'))
