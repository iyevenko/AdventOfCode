test_file = '23_test.txt'
real_file = '23.txt'


def solve():
	elves = set()
	with open(real_file, 'r') as f:
		i = 0
		idx = 0
		lines = f.readlines()
		for y, line in enumerate(lines):
			for x, c in enumerate(line.strip()):
				if c == '#':
					elves.add((x, len(lines)-y-1))

	dirs = [[(0,1), (-1,1), (1,1)],
			[(0,-1), (-1,-1), (1,-1)],
			[(-1,0), (-1,-1), (-1,1)],
			[(1,0), (1,-1), (1,1)],]

	for _ in range(10):
		moves = dict()
		for (x, y) in elves:
			new_pos = None

			for d in dirs:
				if not any((x+dx, y+dy) in elves for (dx, dy) in d):
					new_pos = (x+d[0][0], y+d[0][1])
					break

			if new_pos is None:
				continue

			if new_pos not in moves:
				moves[new_pos] = [(x,y)]
			else:
				moves[new_pos].append((x,y))

		for pos in moves.items():
			new_pos, old_pos = pos
			if len(old_pos) > 1:
				continue

			elves.remove(old_pos[0])
			elves.add(new_pos)

		dirs.append(dirs.pop(0))

	min_x = min(x for x, y in elves)
	max_x = max(x for x, y in elves)
	min_y = min(y for x, y in elves)
	max_y = max(y for x, y in elves)

	return (max_x-min_x+2) * (max_y-min_y+2) - len(elves)


def solve2():
	elves = set()
	with open(real_file, 'r') as f:
		i = 0
		idx = 0
		lines = f.readlines()
		for y, line in enumerate(lines):
			for x, c in enumerate(line.strip()):
				if c == '#':
					elves.add((x, len(lines)-y-1))

	dirs = [[(0,1), (-1,1), (1,1)],
			[(0,-1), (-1,-1), (1,-1)],
			[(-1,0), (-1,-1), (-1,1)],
			[(1,0), (1,-1), (1,1)],]

	i = 0
	moves = [1]
	while len(moves) > 0:
		moves = dict()

		for (x, y) in elves:
			new_pos = None

			count = 0
			for d in dirs:
				if not any((x+dx, y+dy) in elves for (dx, dy) in d):
					if count == 0:
						new_pos = (x+d[0][0], y+d[0][1])
					count += 1

			if new_pos is None or count == 4:
				continue

			if new_pos not in moves:
				moves[new_pos] = [(x,y)]
			else:
				moves[new_pos].append((x,y))

		for pos in moves.items():
			new_pos, old_pos = pos
			if len(old_pos) > 1:
				continue

			elves.remove(old_pos[0])
			elves.add(new_pos)

		dirs.append(dirs.pop(0))
		i += 1

	return i


if __name__ == "__main__":
	print(solve())
	print(solve2())