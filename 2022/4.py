test_file = '4_test.txt'
real_file = '4.txt'


def full_overlap(a, b):
	a1, a2 = [int(x) for x in a]
	b1, b2 = [int(x) for x in b]
	a_in_b = b1 <= a1 and a2 <= b2 
	b_in_a = a1 <= b1 and b2 <= a2 
	return a_in_b or b_in_a

def partial_overlap(a, b):
	a1, a2 = [int(x) for x in a]
	b1, b2 = [int(x) for x in b]

	a_in_b = b1 <= a1 <= b2 or b1 <= a2 <= b2
	b_in_a = a1 <= b1 <= a2 or a1 <= b2 <= a2
	return a_in_b or b_in_a

def solve():
	sum_contains = 0
	with open(real_file, 'r') as f:
		for line in f.readlines():
			a, b = line.strip().split(',')
			res = full_overlap(a.split('-'), b.split('-'))
			sum_contains += int(res)
	return sum_contains


def solve2():
	sum_contains = 0
	with open(real_file, 'r') as f:
		for line in f.readlines():
			a, b = line.strip().split(',')
			res = partial_overlap(a.split('-'), b.split('-'))
			sum_contains += int(res)
	return sum_contains


if __name__ == "__main__":
	print(solve())
	print(solve2())