def v(n, bit):
    return (n >> bit) & 0x1


def calculate_gamma(nums, B):
    sums = []
    for bit in reversed(range(B)):
        s = sum(v(num, bit) for num in nums)
        sums.append(s)
    gamma = ''.join(str(int(x >= len(nums)/2)) for x in sums)
    gamma = int(gamma, base=2)
    return gamma


def solve(f):
    nums = []
    B = 0
    for line in open(f).read().splitlines():
        B = len(line)
        nums.append(int(line, base=2))

    gamma = calculate_gamma(nums, B)
    eps = ~gamma & ((1<<B)-1)
    return gamma * eps


def solve2(f):
    nums = []
    B = 0
    for line in open(f).read().splitlines():
        B = len(line)
        nums.append(int(line, base=2))

    temp_nums = nums.copy()
    for bit in reversed(range(B)):
        gamma = calculate_gamma(temp_nums, B)

        new_nums = []
        for num in temp_nums:
            if not v(num^gamma, bit):
                new_nums.append(num)
        temp_nums = new_nums

        if len(new_nums) == 1:
            oxygen_number = new_nums[0]
            break
    
    temp_nums = nums.copy()
    for bit in reversed(range(B)):
        gamma = calculate_gamma(temp_nums, B)
        eps = ~gamma & ((1<<B)-1)

        new_nums = []
        for num in temp_nums:
            if not v(num^eps, bit):
                new_nums.append(num)
        temp_nums = new_nums

        if len(new_nums) == 1:
            co2_number = new_nums[0]
            break
    
    return oxygen_number * co2_number


if __name__ == '__main__':
    # print(solve('03_test.txt'))
    print(solve('03.txt'))
    # print(solve2('03_test.txt'))
    print(solve2('03.txt'))
