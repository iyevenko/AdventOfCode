test_file = '8_test.txt'
real_file = '8.txt'


def check_mat(mat):
	M = len(mat)
	N = len(mat[0])

	seen = [[0]*N for _ in range(M)]

	# Check left
	for i in range(M):
		max_val = -1
		for j in range(N):
			if mat[i][j] > max_val:
				seen[i][j] = 1
				max_val = mat[i][j]

	# Check top
	for j in range(N):
		max_val = -1	
		for i in range(M):
			if mat[i][j] > max_val:
				seen[i][j] = 1
				max_val = mat[i][j]

	# Check right
	for i in range(M):
		max_val = -1
		for j in reversed(range(N)):
			if mat[i][j] > max_val:
				seen[i][j] = 1
				max_val = mat[i][j]

	# Check bottom
	for j in range(N):
		max_val = -1	
		for i in reversed(range(M)):
			if mat[i][j] > max_val:
				seen[i][j] = 1
				max_val = mat[i][j]

	return seen


def calculate_score(mat, i, j):
	M = len(mat)
	N = len(mat[0])

	d_up = 1
	i2 = i-1
	while i2 >= 0 and mat[i2][j] < mat[i][j]:
		d_up += 1
		i2 -= 1
	if i2 < 0:
		d_up -= 1

	d_down = 1
	i2 = i+1
	while i2 < M and mat[i2][j] < mat[i][j]:
		d_down += 1
		i2 += 1
	if i2 > M-1:
		d_down -= 1

	d_left = 1
	j2 = j-1
	while j2 >= 0 and mat[i][j2] < mat[i][j]:
		d_left += 1
		j2 -= 1
	if j2 < 0:
		d_left -= 1

	d_right = 1
	j2 = j+1
	while j2 < N and mat[i][j2] < mat[i][j]:
		d_right += 1
		j2 += 1
	if j2 > N-1:
		d_right -= 1

	return d_up * d_down * d_left * d_right



def bfb_scores(mat):
	M = len(mat)
	N = len(mat[0])

	scores = [[0]*N for _ in range(M)]

	for i in range(M):
		for j in range(N):
			scores[i][j] = calculate_score(mat, i, j)

	return scores


def read_mat(mat_path):
	mat = []
	with open(mat_path, 'r') as f:
		for line in f.readlines():
			mat.append(list(map(int, line.strip())))
	return mat


def solve():
	mat = read_mat(real_file)
	seen = check_mat(mat)
	num_seen = sum(sum(x) for x in seen)
	return num_seen


def solve2():
	mat = read_mat(real_file)
	scores = bfb_scores(mat)
	best_score = max(max(x) for x in scores)
	return best_score

if __name__ == "__main__":
	print(solve())
	print(solve2())