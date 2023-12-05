def solve(f):
    # 321st place!!
    text = open(f).read()
    seeds, *map_strings = text.split('\n\n')

    seeds = [int(x) for x in seeds.split(': ')[1].split(' ')]
    mappings = []
    for map_str in map_strings:
        mapping = []
        for line in map_str.splitlines()[1:]:
            dst, src, n = [int(x) for x in line.split(' ')]
            mapping.append((src, src+n-1, dst, dst+n-1))
        mappings.append(mapping)

    min_seed = 10000000000000000
    for seed in seeds:
        for mapping in mappings:
            for src1, src2, dst1, dst2 in mapping:
                if src1 <= seed <= src2:
                    seed = dst1 + seed - src1
                    break
        if seed < min_seed:
            min_seed = seed
    return min_seed


def solve2(f):
    text = open(f).read()
    fake_seeds, *map_strings = text.split('\n\n')

    mappings = []
    for map_str in map_strings:
        mapping = []
        for line in map_str.splitlines()[1:]:
            dst, src, n = [int(x) for x in line.split(' ')]
            mapping.append((src, src+n-1, dst, dst+n-1))
        mapping.sort()
        mappings.append(mapping)

    fake_seeds = [int(x) for x in fake_seeds.split(': ')[1].split(' ')]
    seeds = [(start, start+num-1) for start, num in zip(fake_seeds[::2], fake_seeds[1::2])]

    for mapping in mappings:
        new_seeds = []
        for (start, end) in seeds:
            for src1, src2, dst1, dst2 in mapping:
                if start < src1:
                    if end < src1:
                        new_seeds.append((start, end))
                        break
                    if end < src2:
                        new_seeds.append((start, src1-1))
                        new_seeds.append((dst1, end-src1+1))
                        break
                    new_seeds.append((start, src1-1))
                    new_seeds.append((dst1, dst2))
                    start = src2+1
                elif start <= src2:
                    if end <= src2:
                        new_seeds.append((start-src1+dst1, end-src1+dst1))
                        break
                    new_seeds.append((start-src1+dst1, dst2))
                    start = src2+1
            if start > src2:
                new_seeds.append((start, end))
        seeds = new_seeds

    return sorted(seeds)[0][0]

    

if __name__ == '__main__':
    # print(solve('05_test.txt'))
    print(solve('05.txt'))
    # print(solve2('05_test.txt'))
    print(solve2('05.txt'))
