import re


def solve(f):
    s = 0
    for line in open(f).read().splitlines():
        match = re.findall('\d', line)
        s += int(match[0] + match[-1])
    return s


def solve2(f):
    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    reversed_nums = {k[::-1]: v for k, v in nums.items()}

    def first_num(line, nums):
        for i in range(len(line)):
            if line[i].isdigit():
                return int(line[i])
            for j in range(i+3, i+6):
                if line[i:j] in nums:
                    return nums[line[i:j]]
        return 0

    s = 0
    for line in open(f).read().splitlines():
        s += 10 * first_num(line, nums) + first_num(line[::-1], reversed_nums)
    return s


def solve2_fancy(f):
    # REGEX VERSION
    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    s = 0
    for line in open(f).read().splitlines():
        pattern = r'(?=(\d|' + '|'.join(nums.keys()) + r'))'
        matches = re.findall(pattern, line)
        m1, m2 = matches[0], matches[-1]
        m1 = int(m1) if m1.isdigit() else nums[m1]
        m2 = int(m2) if m2.isdigit() else nums[m2]
        s += 10 * m1 + m2
    return s

if __name__ == '__main__':
    # print(solve('01_test1.txt'))
    print(solve('01.txt'))
    # print(solve2('01_test2.txt'))
    print(solve2('01.txt'))
    # print(solve2_fancy('01.txt'))