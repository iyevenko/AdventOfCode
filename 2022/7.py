test_file = '7_test.txt'
real_file = '7.txt'


class File():
	def __init__(self, name, parent, size):
		self.name = name
		self.parent = parent
		self.size = size

	def __repr__(self):
		return self.name

class Dir():
	def __init__(self, name, parent, children=None):
		self.name = name
		self.parent = parent
		self.children = children if children else []
		self._size = None

	@property
	def size(self):
		if self._size is None:
			self._size = sum(map(lambda c: c.size, self.children))
		return self._size

	def add_child(self, child):
		self.children.append(child)

	def get_child(self, name):
		for child in self.children:
			if child.name == name:
				return child
		return None

	def __repr__(self):
		return self.name


def cd(directory, subdirectory):
	if subdirectory == '/':
		return directory
	if subdirectory == '..':
		return directory.parent
	return directory.get_child(subdirectory)


def parse_cmds(lines):
	dirs = []
	root = Dir(parent=None, name='/')
	dirs.append(root)
	curr_dir = root

	i = 0
	while i < len(lines):
		line = lines[i].strip()
		_, cmd, *args = line.split(' ')
		i += 1

		if cmd == 'cd':
			# print(curr_dir, cmd, args[0], curr_dir.children)
			curr_dir = cd(curr_dir, args[0])
		elif cmd == 'ls':
			while i < len(lines) and lines[i][0] != '$':
				line = lines[i].strip()
				info, name = line.split(' ')
				if info == 'dir':
					child = Dir(name=name, parent=curr_dir)
					dirs.append(child)
				else:
					child = File(name=name, parent=curr_dir, size=int(info))
				curr_dir.add_child(child)
				i += 1
	return dirs


def solve():
	size_thresh = 100000
	with open(real_file, 'r') as f:
		dirs = parse_cmds(f.readlines())

	sum_sizes = sum(d.size for d in dirs if d.size <= size_thresh)
	return sum_sizes


def solve2():
	with open(real_file, 'r') as f:
		dirs = parse_cmds(f.readlines())

	del_space = dirs[0].size - 40000000

	min_dir = dirs[0]
	for d in dirs:
		if del_space <= d.size <= min_dir.size:
			min_dir = d
	return min_dir.size



if __name__ == "__main__":
	print(solve())
	print(solve2())