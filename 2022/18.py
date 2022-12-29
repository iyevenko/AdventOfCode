test_file = '18_test.txt'
real_file = '18.txt'



faces = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]


def get_area(pts):
	count = 0
	touching = dict()

	for x, y, z in pts:
		count += 6 - 2 * touching.get((x,y,z), 0)

		for i, j, k in faces:
			p = (x+i,y+j,z+k)
			if p not in touching:
				touching[p] = 0
			touching[p] += 1

	return count, touching


def print_grid(pts, axis=0):
	i, j = [x for x in range(3) if x != axis]
	layers = sorted(pts, key=lambda p: p[axis])

	h = pts[0][axis]
	grid = [['.']*20 for _ in range(20)]
	for p in layers:
		if p[axis] == h:
			up = list(p)
			down = list(p)
			up[axis] += 1
			down[axis] -= 1
			if tuple(up) in pts or tuple(down) in pts:
				grid[p[i]][p[j]] = '@'
			else:
				grid[p[i]][p[j]] = '#'
		else:
			print(f'Layer {h}:')
			for idx, row in enumerate(grid):
				print(f'{idx:2d} ' + ''.join(row))
			print()
			grid = [['.']*20 for _ in range(20)]
			grid[p[i]][p[j]] = '#'
			h = p[axis]

	for idx, row in enumerate(grid):
		print(f'{idx:2d} ' + ''.join(row))
	print()


def solve():
	pts = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			pts.append(tuple(map(int, line.strip().split(','))))
			
	count, _ = get_area(pts)
	return count


def solve2():
	pts = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			pts.append(tuple(map(int, line.strip().split(','))))
			
	count, touching = get_area(pts)

	x_range = [1000, -1]
	y_range = [1000, -1]
	z_range = [1000, -1]

	for p in pts:
		x_range[0] = min(x_range[0], p[0])
		x_range[1] = max(x_range[1], p[0])
		y_range[0] = min(y_range[0], p[1])
		y_range[1] = max(y_range[1], p[1])
		z_range[0] = min(z_range[0], p[2])
		z_range[1] = max(z_range[1], p[2])
		if p in touching:
			touching.pop(p)


	while len(touching) > 0:
		p, num_touching = touching.popitem()
		group = set([p])
		found = True
		while found:
			found = False
			for x,y,z in list(group):
				for i, j, k in faces:
					p = (x+i,y+j,z+k)
					if p not in group:
						if p in touching:
							num_touching += touching.pop(p)
							group.add(p)
							found = True
						elif p not in pts:
							if x_range[0] <= p[0] <= x_range[1] and \
							   y_range[0] <= p[1] <= y_range[1] and \
							   z_range[0] <= p[2] <= z_range[1]:
								group.add(p)
								found = True
							else:
								group = set()
								break
				if len(group) == 0:
					break			

		area, _ = get_area(group)

		if area == num_touching:
			count -= area

	return count


if __name__ == "__main__":
	print(solve())
	print(solve2())