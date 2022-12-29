test_file = '12_test.txt'
real_file = '12.txt'


DIRECTIONS = {
	'^': (-1,0),
	'v': (1,0),
	'<': (0,-1),
	'>': (0,1)
}

class Node():
	_all = []

	def __init__(self, i, j, h, d, path=''):
		self.i = i
		self.j = j
		self.h = h
		self.d = d
		self.path = path
		Node._all.append(self)

	@property
	def pos(self):
		return (self.i, self.j)

	@staticmethod
	def all_nodes():
		return Node._all


def traverse_grid(grid, start, end_nodes, visited=None):
	if visited is None:
		visited = set()
		visited.add(end_nodes[0].pos)

	M = len(grid)
	N = len(grid[0])
	new_nodes = []
	for end_node in end_nodes:
		i1, j1 = end_node.pos

		if (i1, j1) == start:
			return end_node

		h1 = grid[i1][j1]
		d1 = end_node.d

		for d_str, (di, dj) in DIRECTIONS.items():
			i2 = i1 - di
			j2 = j1 - dj
			if 0<=i2<=M-1 and 0<=j2<=N-1 and (i2,j2) not in visited:
				h2 = grid[i2][j2]
				if h1 - h2 <= 1:
					visited.add((i2, j2))
					new_node = Node(i2, j2, h2, d1+1, d_str+end_node.path)
					new_nodes.append(new_node)

	return traverse_grid(grid, start, new_nodes, visited)


def solve():
	grid = []
	with open(real_file, 'r') as f:
		for i, line in enumerate(f.readlines()):
			if 'S' in line:
				start = (i, line.index('S'))
				line = line.replace('S', 'a')
			if 'E' in line:
				end = (i, line.index('E'))
				line = line.replace('E', 'z')
			grid.append([ord(c)-ord('a') for c in line.strip()])

	end_node = Node(*end, ord('z')-ord('a'), 0)
	start_node = traverse_grid(grid, start, [end_node])

	return start_node.d


def solve2():
	grid = []
	with open(real_file, 'r') as f:
		for i, line in enumerate(f.readlines()):
			if 'S' in line:
				start = (i, line.index('S'))
				line = line.replace('S', 'a')
			if 'E' in line:
				end = (i, line.index('E'))
				line = line.replace('E', 'z')
			grid.append([ord(c)-ord('a') for c in line.strip()])

	end_node = Node(*end, ord('z')-ord('a'), 0)
	traverse_grid(grid, start, [end_node])

	shortest = min(n.d for n in Node.all_nodes() if n.h == 0)
	return shortest

if __name__ == "__main__":
	print(solve())
	print(solve2())