test_file = '22_test.txt'
real_file = '22.txt'

import re


def get_lens(grid):
	row_lens = []
	col_lens = []

	M = len(grid)
	N = len(grid[0])

	for i in range(M):
		start = 0
		end = N-1
		while grid[i][start] == ' ':
			start += 1
		while grid[i][end] == ' ':
			end -= 1
		row_lens.append(end-start+1)

	for j in range(N):
		start = 0
		end = M-1
		while grid[start][j] == ' ':
			start += 1
		while grid[end][j] == ' ':
			end -= 1
		col_lens.append(end-start+1)

	return row_lens, col_lens


dirs = ['R', 'D', 'L', 'U']


def traverse(grid, r, c, path):
	M = len(grid)
	N = len(grid[0])

	i = 0
	j = grid[0].index('.')
	dir_idx = 0
	for move in path:
		n = int(move[:-1])
		d = dirs[dir_idx]
		# print(move, d)
		# print(i,j)
		for _ in range(n):
			if d == 'R':
				dj = 1
				if j+1 >= N or grid[i][j+1] == ' ':
					dj -= r[i]
				if grid[i][j+dj] == '#':
					break
				j += dj

			if d == 'L':
				dj = -1
				if j-1 < 0 or grid[i][j-1] == ' ':
					dj += r[i]
				if grid[i][j+dj] == '#':
					break
				j += dj

			if d == 'D':
				di = 1
				if i+1 >= M or grid[i+1][j] == ' ':
					di -= c[j]
				if grid[i+di][j] == '#':
					break
				i += di

			if d == 'U':
				di = -1
				if i-1 < 0 or grid[i-1][j] == ' ':
					di += c[j]
				if grid[i+di][j] == '#':
					break
				i += di

			# print(i, j)

		rot = move[-1]

		if rot == 'R':
			dir_idx = (dir_idx+1)%4 
		elif rot == 'L':
			dir_idx = (dir_idx-1)%4
		# print(dirs[dir_idx])
	return i, j, dirs[dir_idx]


def traverse_cube(faces, face_map, path):
	N = len(faces[1])
	transitions = {
		# (0, j)
		(1, 1): lambda i, j: (0, N-j-1),
		(1, 2): lambda i, j: (N-j-1, N-1),
		(1, 3): lambda i, j: (N-1, j),
		(1, 4): lambda i, j: (j, 0),
		# (i, N-1)
		(2, 1): lambda i, j: (0, N-i-1),
		(2, 2): lambda i, j: (N-i-1, N-1),
		(2, 3): lambda i, j: (N-1, i),
		(2, 4): lambda i, j: (i, 0),
		# (N-1, j)
		(3, 1): lambda i, j: (0, j),
		(3, 2): lambda i, j: (j, N-1),
		(3, 3): lambda i, j: (N-1, N-j-1),
		(3, 4): lambda i, j: (N-j-1, 0),
		# (i, 0)
		(4, 1): lambda i, j: (0, i),
		(4, 2): lambda i, j: (i, N-1),
		(4, 3): lambda i, j: (N-1, N-i-1),
		(4, 4): lambda i, j: (N-i-1, 0)
	}

	face = 1
	grid = faces[face]
	i = 0
	j = 0
	dir_idx = 0
	for move in path:
		n = int(move[:-1])
		d = dirs[dir_idx]
		# print(move, d)
		# print(i,j)
		for _ in range(n):
			if d == 'R':
				if j+1 >= N or grid[i][j+1] == ' ':
					edge = 2
					new_face, new_edge = face_map[(face, edge)]
					new_grid = faces[new_face]
					new_i, new_j = transitions[(edge, new_edge)](i,j)
					if new_grid[new_i][new_j] == '#':
						break
					grid = new_grid
					face = new_face
					i, j = new_i, new_j
					dir_idx = new_edge%4
					d = dirs[dir_idx]
				elif grid[i][j+1] == '#':
					break
				else:
					j += 1

			elif d == 'L':
				if j-1 < 0 or grid[i][j-1] == ' ':
					edge = 4
					new_face, new_edge = face_map[(face, edge)]
					new_grid = faces[new_face]
					new_i, new_j = transitions[(edge, new_edge)](i,j)
					if new_grid[new_i][new_j] == '#':
						break
					grid = new_grid
					face = new_face
					i, j = new_i, new_j
					dir_idx = new_edge%4
					d = dirs[dir_idx]
				elif grid[i][j-1] == '#':
					break
				else:
					j -= 1

			elif d == 'D':
				if i+1 >= N or grid[i+1][j] == ' ':
					edge = 3
					new_face, new_edge = face_map[(face, edge)]
					new_grid = faces[new_face]
					new_i, new_j = transitions[(edge, new_edge)](i,j)
					if new_grid[new_i][new_j] == '#':
						break
					grid = new_grid
					face = new_face
					i, j = new_i, new_j
					dir_idx = new_edge%4
					d = dirs[dir_idx]
				elif grid[i+1][j] == '#':
					break
				else:
					i += 1

			elif d == 'U':
				if i-1 < 0 or grid[i-1][j] == ' ':
					edge = 1
					new_face, new_edge = face_map[(face, edge)]
					new_grid = faces[new_face]
					new_i, new_j = transitions[(edge, new_edge)](i,j)
					if new_grid[new_i][new_j] == '#':
						break
					grid = new_grid
					face = new_face
					i, j = new_i, new_j
					dir_idx = new_edge%4
					d = dirs[dir_idx]
				elif grid[i-1][j] == '#':
					break
				else:
					i -= 1

			# print(face, i, j)

		rot = move[-1]
		if rot == 'R':
			dir_idx = (dir_idx+1)%4 
		elif rot == 'L':
			dir_idx = (dir_idx-1)%4

	print(face, i, j)
	return i, j, dirs[dir_idx], face


def parse_faces_real(grid):
	face_offsets = {
		1: (0, 50),
		2: (0, 100),
		3: (50, 50),
		4: (100, 50),
		5: (100, 0),
		6: (150, 0),
	}
	faces = {
		k: [row[j:j+50] for row in grid[i:i+50]] for k, (i, j) in face_offsets.items()
	}
	face_map = {
		(1, 1): (6, 4),
		(1, 2): (2, 4),
		(1, 3): (3, 1),
		(1, 4): (5, 4),

		(2, 1): (6, 3),
		(2, 2): (4, 2),
		(2, 3): (3, 2),
		(2, 4): (1, 2),

		(3, 1): (1, 3),
		(3, 2): (2, 3),
		(3, 3): (4, 1),
		(3, 4): (5, 1),

		(4, 1): (3, 3),
		(4, 2): (2, 2),
		(4, 3): (6, 2),
		(4, 4): (5, 2),

		(5, 1): (3, 4),
		(5, 2): (4, 4),
		(5, 3): (6, 1),
		(5, 4): (1, 4),

		(6, 1): (5, 3),
		(6, 2): (4, 3),
		(6, 3): (2, 1),
		(6, 4): (1, 1),
	}
	return face_offsets, faces, face_map

def parse_faces_test(grid):
	face_offsets = {
		1: (0, 8),
		2: (4, 0),
		3: (4, 4),
		4: (4, 8),
		5: (8, 8),
		6: (8, 12),
	}
	faces = {
		k: [row[j:j+4] for row in grid[i:i+4]] for k, (i, j) in face_offsets.items()
	}
	face_map = {
		(1, 1): (2, 1),
		(1, 2): (6, 2),
		(1, 3): (4, 1),
		(1, 4): (3, 1),

		(2, 1): (1, 1),
		(2, 2): (3, 4),
		(2, 3): (5, 3),
		(2, 4): (6, 3),

		(3, 1): (1, 4),
		(3, 2): (4, 4),
		(3, 3): (5, 4),
		(3, 4): (2, 2),

		(4, 1): (1, 3),
		(4, 2): (6, 1),
		(4, 3): (5, 1),
		(4, 4): (3, 2),

		(5, 1): (4, 3),
		(5, 2): (6, 4),
		(5, 3): (2, 3),
		(5, 4): (3, 3),

		(6, 1): (4, 2),
		(6, 2): (1, 2),
		(6, 3): (2, 4),
		(6, 4): (5, 2),
	}
	return face_offsets, faces, face_map

def solve():
	grid = []
	with open(real_file, 'r') as f:
		i = 0
		lines = f.readlines()
		N = max(len(l.strip('\n')) for l in lines[:-2])
		while lines[i] != '\n':
			line = [c for c in lines[i].strip('\n')]
			line = line + [' ']*(N-len(line))
			grid.append(line)
			i += 1

		path = re.findall(r'[0-9]+[A-Z]', lines[i+1]+'X')

	row_lens, col_lens = get_lens(grid)

	row, col, facing = traverse(grid, row_lens, col_lens, path)
	score = 1000*(row+1) + 4*(col+1) + dirs.index(facing)
	return score

def solve2(real=True):
	grid = []
	with open(real_file if real else test_file, 'r') as f:
		i = 0
		lines = f.readlines()
		N = max(len(l.strip('\n')) for l in lines[:-2])
		while lines[i] != '\n':
			line = [c for c in lines[i].strip('\n')]
			line = line + [' ']*(N-len(line))
			grid.append(line)
			i += 1

		path = re.findall(r'[0-9]+[A-Z]', lines[i+1]+'X')
		# print(path)

	face_offsets, faces, face_map = parse_faces_real(grid) if real else parse_faces_test(grid)

	row, col, facing, face = traverse_cube(faces, face_map, path)
	oi, oj = face_offsets[face]
	score = 1000*(row+1+oi) + 4*(col+1+oj) + dirs.index(facing)
	return score
	


if __name__ == "__main__":
	print(solve())
	print(solve2(real=True))