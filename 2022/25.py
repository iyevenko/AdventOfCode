test_file = '25_test.txt'
real_file = '25.txt'



def dec_to_snafu(s):
	out = ''
	carry = 0
	while s > 0:
		d, r = divmod(s,5)
		r += carry
		if r < 3:
			out = str(r) + out
			carry = 0
		elif r == 3:
			out = '=' + out
			d += 1
		else:
			out = '-' + out
			d += 1

		s = d
	return out



def solve():
	s = 0
	with open(real_file, 'r') as f:
		for line in f.readlines():
			b = 1
			for c in line.strip()[::-1]:
				if c in '012':
					x = int(c)
				elif c == '-':
					x = -1
				else:
					x = -2
				s += b*x
				b *= 5

	return dec_to_snafu(s)







def solve2():	
	pass



if __name__ == "__main__":
	print(solve())
	print(solve2())