def num_wins(line):
    winners, nums = line.split(': ')[1].split(' | ')
    winners = set(int(x) for x in winners.split(' ') if x)
    nums = set(int(x) for x in nums.split(' ') if x)
    return len(winners & nums)

def solve(f):
    s = 0
    for line in open(f).read().splitlines():
        n = num_wins(line)
        s += 2**(n-1) if n > 0 else 0
    return s

def solve2(f):
    lines = open(f).read().splitlines()
    cards = {i+1: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        for j in range(i+2, i+num_wins(line)+2):
            cards[j] += cards[i+1]
    return sum(cards.values())


if __name__ == '__main__':
    # print(solve('04_test.txt'))
    print(solve('04.txt'))
    # print(solve2('04_test.txt'))
    print(solve2('04.txt'))
