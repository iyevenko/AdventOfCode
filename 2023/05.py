def solve(f):
    text = open(f).read()
    seeds, *map_strings = text.split('\n\n')

    seeds = [int(x) for x in seeds.split(': ')[1].split(' ')]
    maps = []
    for map_str in map_strings:
        map = {}
        for line in map_str.splitlines()[1:]:
            dst, src, n = [int(x) for x in line.split(' ')]
            map[(src, src+n-1)] = (dst, dst+n-1)
        maps.append(map)

    min_seed = 10000000000000000
    for seed in seeds:
        for map in maps:
            for src, dst in map.items():
                if src[0] <= seed <= src[1]:
                    seed = dst[0] + seed - src[0]
                    break
        if seed < min_seed:
            min_seed = seed
    return min_seed


def solve2(f):
    text = open(f).read()
    fake_seeds, *map_strings = text.split('\n\n')

    maps = []
    for map_str in map_strings:
        map = {}
        for line in map_str.splitlines()[1:]:
            dst, src, n = [int(x) for x in line.split(' ')]
            map[(src, src+n-1)] = (dst, dst+n-1)
        maps.append(sorted(map.items()))

    fake_seeds = [int(x) for x in fake_seeds.split(': ')[1].split(' ')]
    seeds = [(start, start + num-1) for start, num in zip(fake_seeds[::2], fake_seeds[1::2])]

    for map in maps:
        new_seeds = []
        for (start, end) in seeds:
            for (src1, src2), (dst1, dst2) in map:
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
