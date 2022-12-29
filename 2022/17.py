test_file = '17_test.txt'
rocks_file = '17_rocks.txt'
real_file = '17.txt'

import re
from tqdm import tqdm
import math
from numpy import base_repr


def parse_shapes(f):
	shapes = []
	for lines in f.read().split('\n\n'):
		lines = lines.split('\n')
		down_edges = []
		left_edges = []
		right_edges = []
		shape = []
		height = 1
		width = 1
		for i, line in enumerate(lines):
			for j, c in enumerate(line):
				if c == '.':
					continue

				shape.append((i,j))
				height = max(height, i+1)
				width = max(width, j+1)
				if j == 0 or (j > 0 and line[j-1] == '.'):
					left_edges.append((i,j))

				if j == len(line)-1 or (j < len(line)-1  and line[j+1] == '.'):
					right_edges.append((i,j))

				if i == len(lines)-1 or (i < len(lines)-1 and lines[i+1][j] == '.'):
					down_edges.append((i,j))

		shapes.append((shape, height, width, down_edges, left_edges, right_edges))
	return shapes


def print_grid(grid, next_shape=None, oi=0, oj=3):
	lines = []
	for row in grid[:-1]:
		lines.append(['|', *['#' if x else '.' for x in row[1:-1]], '|'])
	lines.append(list('+-------+'))

	if next_shape:
		for i, j in next_shape:
			lines[i+oi][j+oj] = '@'

	print()
	for line in lines:
		print(''.join(line))



def get_state(grid):
	# print_grid(grid)

	c = (0, 0)
	p = (0, 1)

	# Set to not 0 or 1
	s = 3
	while p != (0, 7):
		ci, cj = c
		pi, pj = p

		di, dj = pi-ci, pj-cj

		# d = 0,1,2,3 -> u,d,l,r
		d = -1
		if dj == -1 and di > -1:
			pi -= 1	
			d = 0
		elif dj == 1 and di < 1:
			pi += 1
			d = 1
		elif di == 1 and dj > -1:
			pj -= 1
			d = 2
		elif di == -1 and dj < 1:
			pj += 1
			d = 3

		if grid[pi][pj]:
			c = (pi, pj)
		else:
			p = (pi, pj)
			s = (s << 2) | d
	return s


def tetris(shapes, directions, iters=2022):
	grid = [[1]*9]

	dir_idx = 0
	top = 0
	states = dict()
	history = []
	for shape_idx in range(10000):
		shape, h, w, d, l, r = shapes[shape_idx%len(shapes)]

		for _ in range(h+3):
			grid.insert(0, [1]+[0]*7+[1])
		oi, oj = (0, 3)

		state = (get_state(grid), shape_idx%len(shapes), dir_idx%len(directions))
		history.append(top-1)
		if state in states:
			old_idx = states[state]
			x1 = old_idx
			x2 = shape_idx
			y1 = history[old_idx]
			y2 = history[shape_idx]
			n, r = divmod(iters-x1, x2-x1)
			return (history[x1+r]) + n * (y2-y1)

		states[state] = shape_idx

		stopped = False
		while not stopped:
			direction = directions[dir_idx%len(directions)]
			dir_idx += 1

			if direction == '<':
				blocked = False
				for i, j in l:
					if grid[i+oi][j+oj-1]:
						blocked = True
						break
				if not blocked:
					oj -= 1
			else:
				blocked = False
				for i, j in r:
					if grid[i+oi][j+oj+1]:
						blocked = True
						break
				if not blocked:
					oj += 1

			for i, j in d:
				if grid[i+oi+1][j+oj]:
					stopped = True
					break
			if not stopped:
				oi += 1

		for i, j in shape:
			grid[i+oi][j+oj] = 1

		top = max(top, len(grid)-oi)
		grid = grid[-top:]

	return top-1


def solve(iters=2022):
	with open(rocks_file, 'r') as f:
		shapes = parse_shapes(f)

	with open(real_file, 'r') as f:
		height = tetris(shapes, f.read().strip(), iters)

	return height


def solve2():
	return solve(1000000000000)


if __name__ == "__main__":
	print(solve())
	print(solve2())