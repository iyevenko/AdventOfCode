test_file = '13_test.txt'
real_file = '13.txt'


class Packet():
	def __init__(self, s):
		self.s = s
		self._parse_elems(s[1:-1])

	def _parse_elems(self, s):
		self._elems = []
		i = 0
		while i < len(s):
			if s[i] == '[':
				depth = 1
				i2 = i + 1
				while depth > 0:
					if s[i2] == '[':
						depth += 1
					elif s[i2] == ']':
						depth -= 1
					i2 += 1
				self._elems.append(Packet(s[i:i2]))
			else:
				i2 = i + 1
				while i2 < len(s) and s[i2] != ',':
					i2 += 1
				if len(s[i:i2]) > 0:
					self._elems.append(int(s[i:i2]))
			i = i2 + 1

	def __gt__(self, other):
		return compare(self, other) == False

	def __ge__(self, other):
		return compare(self, other) != True

	def __lt__(self, other):
		return compare(self, other) == True

	def __le__(self, other):
		return compare(self, other) != False

	def __getitem__(self, i):
		return self._elems[i]

	def __len__(self):
		return len(self._elems)

	def __repr__(self):
		return '[' + ','.join(str(e) for e in self._elems) + ']'

def compare(l, r):
	if isinstance(l, Packet) and isinstance(r, Packet):
		i = 0
		j = 0
		while True:
			if i >= len(l) and j >= len(r):
				return None
			if i >= len(l):
				return True
			if j >= len(r):
				return False

			res = compare(l[i], r[i])
			if res is not None:
				return res
			i += 1
			j += 1

	if isinstance(l, Packet):
		return compare(l, Packet(f'[{r}]'))

	if isinstance(r, Packet):
		return compare(Packet(f'[{l}]'), r)

	if l == r:
		return None
	return l < r


def insert_sorted(arr, x):
	l = 0
	r = len(arr) - 1

	if x < arr[l]:
		arr.insert(l, x)
		return
	if x > arr[r]:
		arr.insert(r+1, x)
		return

	while l < r:
		m = (l+r)//2
		if x < arr[m]:
			r = m-1
		else:
			l = m+1

	m = (l+r)//2
	if x < arr[m]:
		arr.insert(m, x)
	else:
		arr.insert(m+1, x)


def solve():
	inds = []
	with open(real_file, 'r') as f:
		lines = f.readlines()
		for i, (s1, s2) in enumerate(zip(lines[0::3], lines[1::3])):
			l1 = Packet(s1.strip())
			l2 = Packet(s2.strip())
			if l1 < l2:
				inds.append(i+1)
	return sum(inds)


def solve2():
	packets = [Packet('[[2]]'), Packet('[[6]]')]
	with open(real_file, 'r') as f:
		for line in f.readlines():
			line = line.strip()
			if line:
				insert_sorted(packets, Packet(line))

	key = 1
	for i, p in enumerate(packets):
		if p.s in ['[[2]]', '[[6]]']:
			key *= i+1
	return key

if __name__ == "__main__":
	print(solve())
	print(solve2())