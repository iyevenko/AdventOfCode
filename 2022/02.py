# A/X - Rock
# B/Y - Paper
# C/Z - Scissors

test_file = '2_test.txt'
real_file = '2.txt'

shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
res_scores = [3, 0, 6]

def calculate_points(c1, c2):
	x1 = ord(c1) - ord('A')
	x2 = ord(c2) - ord('X')
	res = (x1-x2)%3
	score = res_scores[res] + shape_scores[c2]
	return score


def convert_to_move(c1, c2):
	# c2 = 'X' -> lose
	# c2 = 'Y' -> draw
	# c2 = 'Z' -> win
	o1 = ord(c1) + ord(c2) - ord('Y')
	o1 = (o1 - ord('A')) % 3 + ord('A')
	o2 = ord('X') - ord('A')
	c2 = chr(o1 + o2)
	return c2


def solve(convert=False):
	pts = 0
	with open(real_file, 'r') as f:
		for l in f.readlines():
			c1, c2 = l.strip().split(' ')
			if convert:
				c2 = convert_to_move(c1, c2)
			pts += calculate_points(c1, c2)
	return pts

def solve2():
	return solve(convert=True)


if __name__ == '__main__':
	print(solve())
	print(solve2())