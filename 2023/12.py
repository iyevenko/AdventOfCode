def num_arrangements(s, groups, curr_group=0, cache={}):
    key = (s, tuple(groups), curr_group)
    if key in cache:
        return cache[key]

    i = 0
    g = groups[0] if groups else 0
    while i < len(s) and s[i] != '?':
        if s[i] == '#':
            curr_group += 1
            if curr_group > g:
                return 0
        elif s[i] == '.' and curr_group:
            if curr_group != g:
                return 0
            curr_group = 0
            groups = groups[1:]
            if groups:
                g = groups[0]
            elif '#' in s[i+1:]:
                return 0
        i += 1
        
    if not groups:
        return int('#' not in s[i:])

    if i == len(s):
        return int(not groups)
    
    total = 0
    # append a '.'
    if curr_group == 0:
        total += num_arrangements(s[i+1:], groups, 0, cache)
    elif curr_group == g:
        total += num_arrangements(s[i+1:], groups[1:], 0, cache)

    # finish a group with a '#'
    if curr_group + 1 == g:
        if s[i+1] == '.':
            total += num_arrangements(s[i+1:], groups[1:], 0, cache)
        elif s[i+1] == '?':
            total += num_arrangements(s[i+2:], groups[1:], 0, cache)
    # add to a group with a '#'
    elif curr_group + 1 < g:
        total += num_arrangements(s[i+1:], groups, curr_group+1, cache)

    cache[key] = total
    return total


def solve(f):
    ret = 0
    for line in open(f).read().splitlines():
        s, g = line.split(' ')
        groups = [int(x) for x in g.split(',')]
        n = num_arrangements(s+'.', groups)
        ret += n
    return ret
    

def solve2(f):
    ret = 0
    for line in open(f).read().splitlines():
        s, g = line.split(' ')
        s = '?'.join([s]*5)
        groups = [int(x) for x in g.split(',')]*5
        n = num_arrangements(s+'.', groups)
        ret += n
    return ret


if __name__ == '__main__':
    # print(solve('12_test.txt'))
    print(solve('12.txt'))
    # print(solve2('12_test.txt'))
    print(solve2('12.txt'))
