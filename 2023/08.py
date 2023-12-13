import math
import parse

def solve(f):
    lines = open(f).read()
    instructions, nodes = lines.split('\n\n')
    edges = {}
    for line in nodes.splitlines():
        node, l, r = parse.parse('{} = ({}, {})', line)
        edges[node] = (l, r)

    node = 'AAA'
    i = 0
    while node != 'ZZZ':
        instr = instructions[i%len(instructions)]
        idx = 0 if instr == 'L' else 1
        node = edges[node][idx]
        i += 1
    return i

def lcm(*args):
    if len(args) == 1:
        return args[0]
    a, *b = args
    lcm_b = lcm(*b)
    return a*lcm_b//math.gcd(a, lcm_b)

def solve2(f):
    z_nodes = set()
    a_nodes = set()
    instructions, nodes = open(f).read().split('\n\n')
    edges = {}
    for line in nodes.splitlines():
        node, l, r = parse.parse('{} = ({}, {})', line)
        edges[node] = (l, r)
        if node.endswith('Z'): z_nodes.add(node)
        if node.endswith('A'): a_nodes.add(node)

    offsets = []
    for node in a_nodes:
        i = 0
        while True:
            if node in z_nodes:
                offsets.append(i)
                break
            
            instr = instructions[i%len(instructions)]
            idx = 0 if instr == 'L' else 1
            node = edges[node][idx]
            i += 1

    return lcm(*offsets)
    

if __name__ == '__main__':
    # print(solve('08_test.txt'))
    print(solve('08.txt'))
    # print(solve2('08_test2.txt'))
    print(solve2('08.txt'))
