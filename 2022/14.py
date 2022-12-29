test_file = '14_test.txt'
real_file = '14.txt'


def render_grid(grid):
	M = len(grid[0])
	print()
	print(' ' + ''.join(f'{x:3d}' for x in range(M)))
	for i, row in enumerate(grid):
		print(f'{i:3d}', row)
	print()


def fill_grid(pts, xlim, ylim):
	x_min, x_max = xlim
	y_min, y_max = ylim

	M = x_max - x_min + 1
	N = y_max + 1

	grid = [[0]*M for _ in range(N)]
	for x, y in pts:
		grid[y][x-x_min] = 1

	return grid


def simulate_sand(grid, x_offset, render=False):
	N = len(grid)
	M = len(grid[0])
	emit_points = (500 - x_offset, 0)
	count = 0
	
	done = False
	while not done:
		x, y = emit_points
		if grid[y][x]:
			done = True
			break
		while True:
			if y + 1 >= N:
				done = True
				break

			if not grid[y+1][x]:
				y += 1
			elif x - 1 < 0:
				done = True
				break
			elif not grid[y+1][x-1]:
				y += 1
				x -= 1
			elif x + 1 >= M:
				done = True
				break
			elif not grid[y+1][x+1]:
				y += 1
				x += 1
			else:
				count += 1
				grid[y][x] = 1
				break
		if render:
			render_grid(grid)
	return count


def parse_lines():
	x_pts = []
	y_pts = []
	with open(real_file, 'r') as f:
		lines = f.readlines()
		for line in lines:
			vertices = line.strip().split(' -> ')
			x1 = None
			y1 = None
			for v in vertices:
				x2, y2 = [int(z) for z in v.split(',')]
				if x1 is not None:
					if x2 != x1:
						for x in range(min(x1, x2), max(x1, x2)+1):
							x_pts.append(x)
							y_pts.append(y1)
					else:
						for y in range(min(y1, y2), max(y1, y2)+1):
							x_pts.append(x1)
							y_pts.append(y)
				x1, y1 = (x2, y2)
	return x_pts, y_pts


def solve(floor=False):
	x_pts, y_pts = parse_lines()

	if floor:
		y_max = max(y_pts)
		y_floor = y_max + 2
		x_floor1 = 500 - y_max - 5
		x_floor2 = 500 + y_max + 6
		for x in range(x_floor1, x_floor2):
			x_pts.append(x)
			y_pts.append(y_floor)

	x_lim = (min(x_pts), max(x_pts))
	y_lim = (min(y_pts), max(y_pts))
	print(x_lim, y_lim)
	grid = fill_grid(zip(x_pts, y_pts), x_lim, y_lim)
	return simulate_sand(grid, x_lim[0])


def solve2():
	return solve(floor=True)

if __name__ == "__main__":
	print(solve())
	print(solve2())