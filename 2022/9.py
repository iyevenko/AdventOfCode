test_file = '9_test.txt'
real_file = '9.txt'


class State():
	moves = {
		'R': (1,0),
		'L': (-1,0),
		'U': (0,1),
		'D': (0,-1),
	}

	def __init__(self, num_tails=1):
		self.head = (0,0)
		self.tails = [(0,0) for _ in range(num_tails)]

	def move_head(self, direction):
		dx, dy = State.moves[direction]
		self.head = (self.head[0]+dx, self.head[1]+dy)

	def move_tails(self):
		head = self.head
		for i in range(len(self.tails)):
			x1, y1 = head
			x2, y2 = self.tails[i]

			dx = x1 - x2
			dy = y1 - y2

			if abs(dx) <= 1 and abs(dy) <= 1:
				pass

			elif abs(dx) > 1:
				if abs(dy) > 0:
					self.tails[i] = (x2 + dx//abs(dx), y2 + dy//abs(dy))
				else:
					self.tails[i] = (x2 + dx//abs(dx), y2)

			elif abs(dy) > 1:
				if abs(dx) > 0:
					self.tails[i] = (x2 + dx//abs(dx), y2 + dy//abs(dy))
				else:
					self.tails[i] = (x2, y2 + dy//abs(dy))

			head = self.tails[i]


def solve(num_tails=1):
	state = State(num_tails)
	tail_positions = set()
	with open(real_file, 'r') as f:
		for line in f.readlines():
			cmd, n = line.strip().split(' ')
			for _ in range(int(n)):
				state.move_head(cmd)
				state.move_tails()
				tail_positions.add(state.tails[-1])
	return len(tail_positions)


def solve2():
	return solve(num_tails=9)

if __name__ == "__main__":
	print(solve())
	print(solve2())