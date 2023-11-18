from math import prod


def solve(f):
    hex_str = open(f).read().strip()
    bits = bin(int(hex_str, base=16))[2:]
    while len(bits)%4 != 0:
        bits = '0' + bits

    def parse(b):
        v, t, b = int(b[:3], base=2), int(b[3:6], base=2), b[6:]
        if t == 4:  # literal value
            h = 1
            while h == 1:
                h, _, b = int(b[0]), b[1:5], b[5:]
            return b, v
        else:
            lt, b = int(b[0], base=2), b[1:]
            if lt == 0:
                l, b = int(b[:15], base=2), b[15:]
                while l > 0:
                    old_len = len(b)
                    b, _v = parse(b)
                    v += _v
                    l -= (old_len - len(b))
            else:
                n, b = int(b[:11], base=2), b[11:]
                while n > 0:
                    b, _v = parse(b)
                    v += _v
                    n -= 1
        return b, v

    _, v = parse(bits)
    return v

def solve2(f):
    hex_str = open(f).read().strip()
    bits = bin(int(hex_str, base=16))[2:]
    while len(bits)%4 != 0:
        bits = '0' + bits

    def parse(b):
        v, t, b = int(b[:3], base=2), int(b[3:6], base=2), b[6:]
        if t == 4:  # literal value
            h = 1
            value = ''
            while h == 1:
                h, part, b = int(b[0]), b[1:5], b[5:]
                value += part
            result = int(value, base=2)
        else:
            operands = []
            lt, b = int(b[0], base=2), b[1:]
            if lt == 0:
                l, b = int(b[:15], base=2), b[15:]
                while l > 0:
                    old_len = len(b)
                    b, value = parse(b)
                    operands.append(value)
                    l -= (old_len - len(b))
            else:
                n, b = int(b[:11], base=2), b[11:]
                while n > 0:
                    b, value = parse(b)
                    operands.append(value)
                    n -= 1

            if t == 0:
                result = sum(operands)
            elif t == 1:
                result = prod(operands)
            elif t == 2:
                result = min(operands)
            elif t == 3:
                result = max(operands)
            elif t == 5:
                x,y = operands
                result = int(x > y)
            elif t == 6:
                x,y = operands
                result = int(x < y)
            elif t == 7:
                x,y = operands
                result = int(x == y)
        return b, result
    
    _, result = parse(bits)
    return result
    

if __name__ == '__main__':
    # print(solve('16_test.txt'))
    print(solve('16.txt'))
    # print(solve2('16_test.txt'))
    print(solve2('16.txt'))
