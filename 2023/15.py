from collections import OrderedDict


def hash(s):
    h = 0
    for c in s:
        h = ((h+ord(c))*17) % 256
    return h

def solve(f):
    steps = open(f).read().strip().split(',')
    return sum(map(hash, steps))

def solve2(f):
    d = {}
    text = open(f).read().strip()
    for op in text.split(','):
        if '=' in op:
            label, val = op.split('=')
            val = int(val)
            key = hash(label)
            if key in d:
                d[key][label] = val
            else:
                d[key] = OrderedDict([(label, val)])

        elif op.endswith('-'):
            label = op[:-1]
            key = hash(label)
            if key in d:
                d[key].pop(label, None)

    s = 0
    for key in d:
        m = (key+1)
        for j, val in enumerate(d[key].values()):
            s += m * (j+1) * val

    return s


if __name__ == '__main__':
    # print(solve('15_test.txt'))
    print(solve('15.txt'))
    # print(solve2('15_test.txt'))
    print(solve2('15.txt'))
