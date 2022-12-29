test_file = '5_test.txt'
real_file = '5.txt'


import parse


def exec_cmd(stacks, qty, src, dst, fifo=False):
	if fifo:
		temp = stacks[src-1][-qty:]
		stacks[src-1] = stacks[src-1][:-qty]
		stacks[dst-1].extend(temp)
	else:
		for _ in range(qty):
			temp = stacks[src-1].pop()
			stacks[dst-1].append(temp)


def parse_boxes(boxes):
	M = len(boxes)
	N = len(boxes[0])

	stacks = [[] for _ in range(N)]

	for j in range(N):
		for i in reversed(range(M)):
			b = boxes[i][j] 
			if b == ' ':
				break
			stacks[j].append(b)

	return stacks


def solve(fifo=False):
	stacks = []
	boxes = []
	cmds = []
	fmt = 'move {0} from {1} to {2}'

	with open(real_file, 'r') as f:
		reading_box = True
		for line in f.readlines():
			if reading_box:
				if line =='\n':
					boxes.pop(-1)
					stacks = parse_boxes(boxes)
					reading_box = False
				else:
					boxes.append(line[1:-1:4])
			else:
				parsed = parse.parse(fmt, line)
				parsed = [int(x.strip()) for x in parsed]
				exec_cmd(stacks, *parsed, fifo)

	msg = ''
	for s in stacks:
		msg += s.pop()
	return msg


def solve2():
	return solve(fifo=True)


if __name__ == "__main__":
	print(solve())
	print(solve2())