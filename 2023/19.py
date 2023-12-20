from math import prod


def process_part(w, part):
    workflow = w['in']
    while True:
        for rule in workflow:
            dest = rule(part)
            if dest == 'A':
                return True
            elif dest == 'R':
                return False
            elif dest in w:
                workflow = w[dest]
                break

def solve(f):
    workflows, parts = open(f).read().split('\n\n')
    w = {}
    for line in workflows.splitlines():
        name, rules = line.strip().split('{')
        rules = rules[:-1]
        w[name] = []
        *rules, default = rules.split(',')
        for rule in rules:
            cond, dest = rule.split(':')
            if '>' in cond:
                key, val = cond.split('>')
                val = int(val)
                w[name].append(lambda x, key=key, val=val, dest=dest: dest if x[key] > val else None)
            elif '<' in cond:
                key, val = cond.split('<')
                val = int(val)
                w[name].append(lambda x, key=key, val=val, dest=dest: dest if x[key] < val else None)
        w[name].append(lambda x, default=default: default)

    s = 0
    for part in parts.splitlines():
        part = eval(f"dict({part.strip('{}')})")
        if process_part(w, part):
            s += sum(part.values())

    return s


def calculate_ranges(ranges, workflow_name, w):
    num_accepted = 0
    workflow = w[workflow_name]
    ranges = ranges.copy()
    for rule in workflow:
        key, op, val, dest = rule
        m, M = ranges[key]
        true_ranges = ranges.copy()
        if op == '>':
            if m > val:
                true_ranges[key] = (m, M)
                ranges = None
            elif M > val:
                true_ranges[key] = (val+1, M)
                ranges[key] = (m, val)
            else:
                true_ranges = None
                ranges[key] = (m, M)
        elif op == '<':
            if M < val:
                true_ranges[key] = (m, M)
                ranges = None
            elif m < val:
                true_ranges[key] = (m, val-1)
                ranges[key] = (val, M)
            else:
                true_ranges = None
                ranges[key] = (m, M)

        if true_ranges:
            if dest == 'A':
                num_accepted += prod([M-m+1 for m, M in true_ranges.values()])
            elif dest in w:
                num_accepted += calculate_ranges(true_ranges, dest, w)

    return num_accepted

    
def solve2(f):
    workflows, parts = open(f).read().split('\n\n')
    w = {}
    for line in workflows.splitlines():
        name, rules = line.strip().split('{')
        rules = rules[:-1]
        w[name] = []
        *rules, default = rules.split(',')
        for rule in rules:
            cond, dest = rule.split(':')
            if '>' in cond:
                key, val = cond.split('>')
                val = int(val)
                w[name].append((key, '>', val, dest))
            elif '<' in cond:
                key, val = cond.split('<')
                val = int(val)
                w[name].append((key, '<', val, dest))
        w[name].append(('a', '>', 0, default))

    ranges = {k: (1, 4000) for k in 'xmas'}
    return calculate_ranges(ranges, 'in', w)
    

if __name__ == '__main__':
    # print(solve('19_test.txt'))
    print(solve('19.txt'))
    # print(solve2('19_test.txt'))
    print(solve2('19.txt'))
