def check_line(line):
    q = []
    score_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for c in line:
        if c in '{[(<':
            q.append(c)
        elif c == '}':
            if q[-1] == '{':
                q.pop()
            else:
                return score_lookup[c]
        elif c == ']':
            if q[-1] == '[':
                q.pop()
            else:
                return score_lookup[c]
        elif c == ')':
            if q[-1] == '(':
                q.pop()
            else:
                return score_lookup[c]
        elif c == '>':
            if q[-1] == '<':
                q.pop()
            else:
                return score_lookup[c]
    return 0    


def fix_line(line):
    q = []
    score = 0

    for c in line:
        if c in '{[(<':
            q.append(c)
        elif c == '}':
            if q[-1] == '{':
                q.pop()
            else:
                return 0
        elif c == ']':
            if q[-1] == '[':
                q.pop()
            else:
                return 0
        elif c == ')':
            if q[-1] == '(':
                q.pop()
            else:
                return 0
        elif c == '>':
            if q[-1] == '<':
                q.pop()
            else:
                return 0
            
    score_lookup = {'(': 1, '[': 2, '{': 3, '<': 4}
    print(''.join(q))
    for c in reversed(q):
        score = score * 5 + score_lookup[c]
    return score


def solve(f):
    score = 0
    for line in open(f).read().splitlines():
        s = check_line(line)
        score += s
    return score

def solve2(f):
    scores = []
    for line in open(f).read().splitlines():
        s = fix_line(line)
        if s:
            scores.append(s)
    return sorted(scores)[len(scores)//2]
    

if __name__ == '__main__':
    # print(solve('10_test.txt'))
    # print(solve('10.txt'))
    # print(solve2('10_test.txt'))
    print(solve2('10.txt'))
