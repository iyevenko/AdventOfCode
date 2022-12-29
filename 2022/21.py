test_file = '21_test.txt'
real_file = '21.txt'


graph = dict()


class Node():
	def __init__(self):
		pass


class Operator(Node):
	def __init__(self, inputs):
		self.inputs = inputs

class add(Operator):
	def __init__(self, inputs):
		self.inputs = inputs

	def forward(self, inputs):
		a, b = inputs
		return a + b

	def backward(self, inputs, out):
		a, b = inputs
		return out - b, out - a

class subtract(Operator):
	def __init__(self, inputs):
		self.inputs = inputs

	def forward(self, inputs):
		a, b = inputs
		return a - b

	def backward(self, inputs, out):
		a, b = inputs
		return out + b, a - out

class multiply(Operator):
	def __init__(self, inputs):
		self.inputs = inputs

	def forward(self, inputs):
		a, b = inputs
		return a * b

	def backward(self, inputs, out):
		a, b = inputs
		return out / b , out / a

class divide(Operator):
	def __init__(self, inputs):
		self.inputs = inputs

	def forward(self, inputs):
		a, b = inputs
		return a / b

	def backward(self, inputs, out):
		a, b = inputs
		return out * b, a / out

class equal(Operator):
	def __init__(self, inputs):
		self.inputs = inputs

	def forward(self, inputs):
		a, b = inputs
		return a == b

	def backward(self, inputs, out):
		a, b = inputs
		if out:
			return b, a
		# This could be anything as long as they're not equal
		return a, a+1

Node.__add__ = lambda self, other: add(self, other)
Node.__sub__ = lambda self, other: subtract(self, other)
Node.__mul__ = lambda self, other: multiply(self, other)
Node.__truediv__ = lambda self, other: divide(self, other)
Node.__eq__ = lambda self, other: equal(self, other)


class Constant(Node):
	def __init__(self, val):
		super().__init__()
		self.val = val


OPS = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
	'=': equal
}


def dfs(node, order, vis=set()):
    if node not in vis:
        vis.add(node)
        if isinstance(node, Operator):
            for input_node in node.inputs:
                dfs(graph[input_node], order)
        order.append(node)


def forward_pass(order):
	for node in order:
		if isinstance(node, Operator):
			node.val = node.forward([graph[prev].val for prev in node.inputs])

def backward_pass(order, target):
	seen = set()
	for node in reversed(order):
		if isinstance(node, Operator):
			backs = node.backward([graph[prev].val for prev in node.inputs], node.back)
			for inp, back in zip(node.inputs, backs):
				if inp == target:
					return back

				assert inp not in seen, f'Node received conflicting backward values: {inp.back}, {back}'
				graph[inp].back = back
				seen.add(inp)

def solve(order=None, replace_equals=False):
	with open(real_file, 'r') as f:
		for line in f.readlines():
			name, val = line.strip().split(': ')
			try:
				node = Constant(int(val))
			except ValueError:
				l, op_key, r = val.split(' ')
				if replace_equals and name == 'root':
					op_key = '='
				op = OPS[op_key]
				node = op([l, r])
			graph[name] = node

	if order is None:
		order = []
	dfs(graph['root'], order)
	forward_pass(order)

	return int(graph['root'].val)

def solve2():
	order = []
	solve(order, replace_equals=True)
	graph['root'].back = True
	back = backward_pass(order, target='humn')
	return int(back)


if __name__ == "__main__":
	print(solve())
	print(solve2())