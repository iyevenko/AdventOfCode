test_file = '1_test.txt'
real_file = '1.txt'


def insert_sorted(arr, x):
	idx = 2
	if cur_sum > max_sums[2]:
		if cur_sum > max_sums[1]:
			max_sums[2] = max_sums[1]
			idx -= 1
			if cur_sum > max_sums[0]:
				max_sums[1] = max_sums[0]
				idx -= 1
	else:
		return

	arr[idx] = x

def solve():
	max_sums = [-1,-1,-1]
	cur_sum = 0
	with open(real_file, 'r') as f:
		for l in f.readlines():
			l = l.strip()
			if l:
				cur_sum += int(l)
			else:
				insert_sorted(max_sums, cur_sum)
				cur_sum = 0
	insert_sorted(max_sums, cur_sum)
	return max_sums


if __name__ == '__main__':	
	max_sums = solve()
	print(max_sums[0])
	print(sum(max_sums))