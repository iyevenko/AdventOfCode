from functools import lru_cache
import parse


def solve(f):
    p1, p2 = parse.parse('Player 1 starting position: {:d}\nPlayer 2 starting position: {:d}', open(f).read().strip())
    
    n = 0
    s1 = 0
    s2 = 0
    while True:
        p1 = (p1 + 18*n + 6-1) % 10 + 1
        p2 = (p2 + 18*n + 15-1) % 10 + 1
        s1 += p1
        if s1 >= 1000:
            return (6*n + 3) * s2
        s2 += p2
        if s2 >= 1000:
            return (6*n + 6) * s1
        n += 1

def solve2(f):
    p1, p2 = parse.parse('Player 1 starting position: {:d}\nPlayer 2 starting position: {:d}', open(f).read().strip())
    sums = {}
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                sums[i+j+k] = sums.get(i+j+k, 0) + 1
    
    @lru_cache
    def step(p, roll):
        return (p + roll - 1) % 10 + 1

    @lru_cache
    def p1_wins_losses(p1, s1, p2, s2):
        # Number of wins/losses for player 1 given starting state
        wins = 0
        losses = 0
        for roll1, n1 in sums.items():
            p1_new = step(p1, roll1)
            s1_new = s1 + p1_new
            if s1_new >= 21:
                wins += n1
                continue
            for roll2, n2 in sums.items():
                p2_new = step(p2, roll2)
                s2_new = s2 + p2_new
                if s2_new < 21:
                    w, l = p1_wins_losses(p1_new, s1_new, p2_new, s2_new)
                    wins += n1 * n2 * w
                    losses += n1 * n2 * l
                else:
                    losses += n1 * n2
        return wins, losses
    
    return max(p1_wins_losses(p1, 0, p2, 0))
    

if __name__ == '__main__':
    # print(solve('21_test.txt'))
    print(solve('21.txt'))
    # print(solve2('21_test.txt'))
    print(solve2('21.txt'))
