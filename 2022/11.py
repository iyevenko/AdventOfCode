test_file = '11_test.txt'
real_file = '11.txt'

import parse

class Monkey():
	worry = False
	divisor = 1

	def __init__(self, idx, items, op, test_func):
		self.idx = idx
		self.items = items
		self.op = op
		self.test_func = test_func
		self.inspection_count = 0

	def calculate_destination(self, item):
		worry_level = item
		worry_level = self.op(worry_level)
		if not Monkey.worry:
			worry_level = worry_level//3
		else:
			worry_level = worry_level % Monkey.divisor
		dest = self.test_func(worry_level)
		return dest, worry_level

	def go(self):
		actions = []
		self.inspection_count += len(self.items)
		for item in self.items:
			dest, worry_level = self.calculate_destination(item)
			actions.append((dest, worry_level))
		self.items = []
		return actions



fmts = [
	"Monkey {:d}:",
	"  Starting items: {}",
	"  Operation: new = old {}",
	"  Test: divisible by {:d}",
	"    If true: throw to monkey {:d}",
	"    If false: throw to monkey {:d}"
]


def parse_op_string(s):
	op, val = s.split(' ')
	op_name = '__add__' if op == '+' else '__mul__'

	def func(x):
		y = x if val == 'old' else int(val)
		return getattr(x, op_name)(y)
	return func


def parse_test_func(divisor, true_id, false_id):
	def func(x):
		return true_id if x % divisor == 0 else false_id
	return func


def solve(iters=20, worry=False):
	Monkey.worry = worry

	with open(real_file, 'r') as f:
		lines = f.readlines()

	monkeys = dict()
	i = 0
	while i < len(lines):
		parsed_lines = []

		for j, fmt in enumerate(fmts):
			parsed_lines.append(parse.parse(fmt, lines[i+j].strip('\n'))[0])

		idx = parsed_lines[0]
		items = [int(x) for x in parsed_lines[1].split(', ')]
		op = parse_op_string(parsed_lines[2])
		divisor = parsed_lines[3]
		true_id = parsed_lines[4]
		false_id = parsed_lines[5]
		test_func = parse_test_func(divisor, true_id, false_id)

		monkey = Monkey(idx, items, op, test_func)
		monkeys[idx] = monkey
		Monkey.divisor *= divisor

		i += len(fmts) + 1

	for i in range(iters):
		for k in sorted(monkeys.keys()):
			actions = monkeys[k].go()
			for dest, worry_level in actions:
				monkeys[dest].items.append(worry_level)

	top2 = sorted([m.inspection_count for m in monkeys.values()])[-2:]
	return top2[0] * top2[1]


def solve2():
	return solve(iters=10000, worry=True)

if __name__ == "__main__":
	print(solve())
	print(solve2())