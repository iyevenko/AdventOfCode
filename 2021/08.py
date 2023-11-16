def decode_line(line):
    train, test = line.split(' | ')
    train = [set(d) for d in train.split(' ')]
    test = [set(d) for d in test.split(' ')]

    lens = {i: [] for i in range(2, 8)}
    for s in train:
        lens[len(s)].append(s)

    digits = {}
    [digits[1]] = lens[2]
    [digits[7]] = lens[3]
    [digits[4]] = lens[4]
    [digits[8]] = lens[7]
    [digits[9]] = [d for d in lens[6] if len(d - digits[4]) == 2]
    [digits[0]] = [d for d in lens[6] if digits[1].issubset(d) and d != digits[9]]
    [digits[6]] = [d for d in lens[6] if d != digits[0] and d != digits[9]]
    [digits[2]] = [d for d in lens[5] if len(digits[9] - d) != 1]
    [digits[3]] = [d for d in lens[5] if len(d - digits[2]) == 1]
    [digits[5]] = [d for d in lens[5] if d != digits[2] and d != digits[3]]

    # for k in sorted(digits):
    #     print(k, ''.join(sorted(digits[k])))

    set2digit = {''.join(sorted(v)): k for k, v in digits.items()}
    decoded = [set2digit[''.join(sorted(x))] for x in test]
    return decoded


def solve(f):
    s = 0
    for line in open(f).read().splitlines():
        decoded = decode_line(line)
        s += len([d for d in decoded if d in {1, 4, 7, 8}])
    return s

def solve2(f):
    s = 0
    for line in open(f).read().splitlines():
        d = decode_line(line)
        s += 1000*d[0] + 100*d[1] + 10*d[2] + d[3]
    return s
    

if __name__ == '__main__':
    # print(solve('08_test.txt'))
    print(solve('08.txt'))
    # print(solve2('08_test.txt'))
    print(solve2('08.txt'))
