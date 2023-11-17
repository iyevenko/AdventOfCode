def solve(f):
    template, mappings = open(f).read().split('\n\n')
    polymap = {}
    for s in mappings.splitlines():
        k, v = s.strip().split(' -> ')
        polymap[k] = v
    
    for _ in range(10):
        new_template = ""
        for i in range(len(template)-1):
            sub = template[i:i+2]
            new_template += sub[0] + polymap.get(sub, '')
        template = new_template + template[-1]
    
    occurances = {}
    for c in template:
        occurances[c] = occurances.get(c, 0) + 1
    
    sorted_keys = sorted(occurances, key=lambda k: occurances[k])
    return occurances[sorted_keys[-1]] - occurances[sorted_keys[0]]


def solve2(f, max_depth=40):
    template, mappings = open(f).read().split('\n\n')
    polymap = {}
    for s in mappings.splitlines():
        k, v = s.strip().split(' -> ')
        polymap[k] = v
    
    def merge_counts(c1, c2):
        c3 = {}
        for k in c1.keys() & c2.keys():
            c3[k] = c1[k] + c2[k]
        for k in c2.keys() - c1.keys():
            c3[k] = c2[k]
        for k in c1.keys() - c2.keys():
            c3[k] = c1[k]
        return c3

    cache = {}
    def dfs(s, depth=1):
        a, b = s
        c = polymap[s]
        counts = {c: 1}
        if depth == max_depth:
            return counts

        for s2 in [a+c, c+b]:
            key = (s2, max_depth-depth)
            if key in cache:
                new_counts = cache[key]
            else:
                new_counts = dfs(s2, depth+1)
                cache[key] = new_counts
            counts = merge_counts(counts, new_counts)
        return counts
    
    counts = {}
    for c in template:
        counts[c] = counts.get(c, 0) + 1
    for i in range(len(template)-1):
        sub = template[i:i+2]
        new_counts = dfs(sub)
        counts = merge_counts(counts, new_counts)

    sorted_keys = sorted(counts, key=lambda k: counts[k])
    return counts[sorted_keys[-1]] - counts[sorted_keys[0]]

if __name__ == '__main__':
    # print(solve('14_test.txt'))
    print(solve('14.txt'))
    # print(solve2('14_test.txt'))
    print(solve2('14.txt'))
