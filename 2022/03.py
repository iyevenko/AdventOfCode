test_file = '3_test.txt'
real_file = '3.txt'


def get_priority(c):
	priority = ord(c.lower()) - ord('a') + 1
	if c.isupper():
		priority += 26
	return priority


def get_priorities(s):
	N = len(s)
	s1 = s[:N//2]
	s2 = s[N//2:]

	left = set(s1)
	right = set(s2)

	inter = left.intersection(right)
	priorities = [get_priority(c) for c in inter]
	return priorities


def solve():
	sum_priorities = 0
	with open(real_file, 'r') as f:
		for line in f.readlines():
			p = get_priorities(line.strip())
			sum_priorities += sum(p)
	return sum_priorities


def solve2():
	sum_priorities = 0
	with open(real_file, 'r') as f:
		s = []
		for i, line in enumerate(f.readlines()):
			c = set(line.strip())
			s.append(set(c))
			if i % 3 == 2:
				inter = s[0].intersection(s[1]).intersection(s[2])
				sum_priorities += sum(get_priority(c) for c in inter)
				s = []
	return sum_priorities



if __name__ == "__main__":
	print(solve())
	print(solve2())