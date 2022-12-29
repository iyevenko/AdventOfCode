test_file = '6_test.txt'
real_file = '6.txt'


def check_start(buf):
	s = set()
	for c in buf:
		if c in s:
			return False
		s.add(c)
	return True

def get_start(s, n):
	buf = s[:n]

	for i, c in enumerate(s[n:]):
		if check_start(buf):
			return i + n
		buf = buf[1:] + c
	return -1


def solve(n=4):
	starts = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			start = get_start(line.strip(), n)
			starts.append(start)
	#print(starts)
	return start


def solve2():
	return solve(n=14)


if __name__ == "__main__":
	print(solve())
	print(solve2())