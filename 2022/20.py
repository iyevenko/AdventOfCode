test_file = '20_test.txt'
real_file = '20.txt'


def solve(key=1, rounds=1):
	arr = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			arr.append(key*int(line.strip()))

	N = len(arr)
	arr_mod = list(map(lambda x: x%(N-1), arr))
	inds = {i: i for i in range(N)}
	for _ in range(rounds):
		for n in range(N):
			x = arr_mod[n]
			if x == 0:
				continue

			i = inds[n]
			j = i + x

			if j >= N-1: 
				j += 1
			elif j <= 0:
				j -= 1
			# Theoretically this can be O(|x|+log(N))
			# Implement binary search to find v's such that i < v <= j%N
			# Loop over all |x| of these
			# Basically makes the whole algo E[|x|]/N faster (|x|<N due to modulo)
			for k,v in list(inds.items()):
				if i < v <= j%N:
					inds[k] -= 1
				elif j%N <= v < i:
					inds[k] += 1

			inds[n] = j%N


	new_arr = arr.copy()
	zero = 0
	for k, v in inds.items():
		new_arr[v] = arr[k]
		if arr[k] == 0:
			zero = k

	return sum(new_arr[(inds[zero]+x)%N] for x in [1000, 2000, 3000])



def solve2():
	return solve(key=811589153, rounds=10)


if __name__ == "__main__":
	print(solve())
	print(solve2())