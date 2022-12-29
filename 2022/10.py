test_file = '10_test.txt'
real_file = '10.txt'

def solve():
	t = 0
	x = 1
	strengths = 0
	with open(real_file, 'r') as f:
		for line in f.readlines():
			op, *val = line.strip().split(' ')

			t += 1
			if t % 40 == 20:
				strengths += t * x

			if op == 'addx':
				t += 1
				if t % 40 == 20:
					strengths += t * x
				x += int(val[0])

	return strengths


def solve2():
	t = 0
	x = 1
	crt = [['.']*40 for _ in range(6)]
	with open(real_file, 'r') as f:
		for line in f.readlines():
			op, *val = line.strip().split(' ')

			i, j = divmod(t, 40)
			if x-1 <= j <= x+1:
				crt[i][j] = '#'
			t += 1


			if op == 'addx':
				i, j = divmod(t, 40)
				if x-1 <= j <= x+1:
					crt[i][j] = '#'
				t += 1

				x += int(val[0])
	return '\n'.join(''.join(x) for x in crt)

if __name__ == "__main__":
	print(solve())
	print(solve2())