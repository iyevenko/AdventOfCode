test_file = '15_test.txt'
real_file = '15.txt'

import parse
from tqdm import tqdm


class Range():
	def __init__(self, start=None, stop=None):
		if start is None:
			if stop is None:
				self.slices = []
			else:
				self.slices = [(start, start)]
		else:
			self.slices = [(start, stop)]

	def __len__(self):
		return sum(j-i+1 for i,j in self.slices)

	def __contains__(self, item):
		return any(self.slices_interect(s, (item, item)) for s in self.slices)

	def add_slice(self, start, stop):
		merged_slices = [(start, stop)]
		unmerged_slices = []
		for s in self.slices:
			if self.slices_interect(s, (start, stop)):
				merged_slices.append(s)
			else:
				unmerged_slices.append(s)
		self.slices = unmerged_slices + [self.merge_slices(merged_slices)]

	def merge_slices(self, slices):
		i = min(s[0] for s in slices)
		j = max(s[1] for s in slices)
		return (i,j)

	def slices_interect(self, s1, s2):
		i1, j1 = s1
		i2, j2 = s2
		return i1-1<=i2<=j1+1 or i1-1<=j2<=j1+1 or i2-1<=i1<=j2+1 or i2-1<=j1<=j2+1 



def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1-x2) + abs(y1-y2)


def parse_line(line):
	fmt = "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}"
	sx, sy, bx, by = parse.parse(fmt, line)
	return (sx, sy), (bx, by)


def solve(real=True):
	if real:
		y = 2000000
		file = real_file
	else:
		y = 10
		file = test_file

	beacons = set()
	no_beacon = set()
	x_range = Range()
	with open(file, 'r') as f:
		for line in f.readlines():
			s, b = parse_line(line.strip())
			beacons.add(b)

			sx, sy = s

			row_range = distance(s, b) - abs(sy - y)
			if row_range > 0:
				x_range.add_slice(sx-row_range, sx+row_range)

	count = len(x_range)

	for bx, by in beacons:
		if by == y and bx in x_range:
			count -= 1

	return count


def solve2(real=True):
	if real:
		ys = range(4000000+1)
		file = real_file
	else:
		ys = range(20+1)
		file = test_file

	sensors = []
	distances = []
	with open(file, 'r') as f:
		for line in f.readlines():
			s, b = parse_line(line.strip())
			d = distance(s, b)
			sensors.append(s)
			distances.append(d)


	for y in tqdm(ys):
		x_range = Range()

		for s, d in zip(sensors, distances):
			sx, sy = s
			row_range = d - abs(sy - y)
			if row_range > 0:
				x_range.add_slice(sx-row_range, sx+row_range)
				
		if len(x_range.slices) == 2:
			x = x_range.slices[0][1]+1
			return 4000000*x + y
	return


if __name__ == "__main__":
	print(solve())
	print(solve2())