test_file = '16_test.txt'
real_file = '16.txt'

import re
from tqdm import tqdm
import math


def parse_line(line):
	name, *valves = re.findall(r'[A-Z]{2}', line)
	rate = int(re.findall(r'[0-9]+', line)[0])
	return name, rate, valves


def calculate_distances(v):
	remaining = set()
	d = dict()

	for k1 in v.keys():
		d[k1] = dict()
		for k2 in v.keys():
			if k1 == k2:
				d[k1][k2] = 0
			else:
				remaining.add((k1, k2))
				d[k1][k2] = math.inf

	for k1, (_, valves) in v.items():
		for valve in valves:
			d[k1][valve] = 1
			remaining.remove((k1, valve))

	while remaining:
		done = set()
		for k1, k2 in remaining:
			d_min = math.inf
			for k_mid, dist in d[k1].items():
				d_min = min(d_min, d[k_mid][k2] + dist)
			if d_min < math.inf:
				d[k1][k2] = d_min
				done.add((k1, k2))
		remaining -= done

	return d


def search(v, d, curr='AA', t=30, opened=set(), cache=dict()):
	if t <= 0:
		return 0

	# For speedup, can use bitmask
	opened_str = ''.join(sorted(opened))
	state = (curr, t, opened_str)
	if state in cache:
		return cache[state]

	p_max = 0
	for k, (rate, _) in v.items():
		if k in opened:
			continue

		dt = d[curr][k]+1
		payoff = max(t-dt, 0) * rate
		if payoff == 0:
			continue

		p_max = max(p_max, payoff + search(v, d, k, t-dt, opened.union({k}), cache))

	cache[state] = p_max
	return p_max



def elephant_search(v, d, curr1='AA', curr2='AA', t1=26, t2=26, opened=set(), cache=dict()):
	if t1 <= 0 and t2 <= 0:
		return 0

	opened_str = ''.join(sorted(opened))
	state = (curr1, curr2, t1, t2, opened_str)
	if state in cache:
		return cache[state]

	if t1 >= t2:
		t = t1
		curr = curr1
	else:
		t = t2
		curr = curr2

	p_max = 0
	for k, (rate, _) in v.items():
		if k in opened:
			continue

		dt = d[curr][k]+1
		payoff = max(t-dt, 0) * rate
		if payoff == 0:
			continue

		if t1 >= t2:
			p_max = max(p_max, payoff + elephant_search(v, d, k, curr2, t-dt, t2, opened.union({k})))
		else:
			p_max = max(p_max, payoff + elephant_search(v, d, curr1, k, t1, t-dt, opened.union({k})))

	cache[state] = p_max
	return p_max


def print_distance_matrix(d):
	print(' '*4 + ' '.join(d.keys()))
	for name, row in d.items():
		print(name, end=' ')
		print(''.join(map(lambda r: f'{r:3d}', row.values())))


def solve(with_elephant=False):
	v = dict()

	with open(real_file, 'r') as f:
		for line in f.readlines():
			name, rate, valves = parse_line(line.strip())
			v[name] = (rate, valves)

	d = calculate_distances(v)
	# print_distance_matrix(d)

	if with_elephant:
		payoff = elephant_search(v, d)
	else:
		payoff = search(v, d)
	return payoff


def solve2():
	return solve(with_elephant=True)


if __name__ == "__main__":
	print(solve())
	print(solve2())