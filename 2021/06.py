from collections import deque

def solve(f, N=80):
    fish = sorted(map(int, open(f).read().strip().split(',')))
    fish_counts = deque([0]*9, maxlen=9)
    for f in fish:
        fish_counts[f] += 1

    for _ in range(N):
        n_new = fish_counts.popleft()
        fish_counts[6] += n_new
        fish_counts.append(n_new)
    
    return sum(fish_counts)


def solve2(f):
    return solve(f, N=256)

if __name__ == '__main__':
    # print(solve('06_test.txt'))
    print(solve('06.txt'))
    # print(solve2('06_test.txt'))
    print(solve2('06.txt'))