test_file = '24_test.txt'
real_file = '24.txt'

from math import gcd, lcm
import math
from collections import deque


import sys
sys.setrecursionlimit(2000)

def step(blizzard, M, N):
	bliz = dict()
	for (i_, j_), v in blizzard.items():
		for d in v:
			i = i_
			j = j_
			if d == '>':
				j += 1
				if j == N-1:
					j = 1
			if d == 'v':
				i += 1
				if i == M-1:
					i = 1
			if d == '<':
				j -= 1
				if j == 0:
					j = N-2
			if d == '^':
				i -= 1
				if i == 0:
					i = M-2

			if (i,j) in bliz:
				bliz[(i,j)].append(d)
			else:
				bliz[(i,j)] = [d]
	return bliz


def dfs(grid, blizzards, pos, end, num_states, t=0, cache=dict(), path=set(), best=math.inf, reverse=False):
	i,j = pos
	state = (t, pos)
	true_state = (t%num_states, pos)

	if (i,j) == end:
		# print(f'REACHED END: {t}')
		return t

	if true_state in path or t > best:
		return math.inf

	if state in cache:
		# print(f'USING CACHED', t, cache[state])
		return t + cache[state]

	if reverse:
		moves = [(0,-1),(-1,0),(0,1),(1,0),(0,0)]
	else:
		moves = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]

	blizzard = blizzards[t%num_states]
	new_best = math.inf
	for di, dj in moves:
		new_pos = (i+di, j+dj)
		in_grid = 0 <= i+di <= len(grid)-1 and 0 < j+dj < len(grid[0])-1
		if new_pos in blizzard or not in_grid or grid[i+di][j+dj]:
			continue

		time = dfs(grid, blizzards, new_pos, end, num_states, t+1, cache, path.union({true_state}), min(new_best, best), reverse)
		new_best = min(new_best, time)

	cache[state] = new_best - t
	return new_best


def bfs(grid, blizzards, pos, end, num_states, start_time=0):
	moves = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]
	q = deque()
	q.append((start_time, pos))
	seen = set()
	while q:
		t, (i,j) = q.popleft()

		state = (t%num_states, (i,j))
		if state in seen:
			continue
		seen.add(state)

		if (i,j) == end:
			return t

		blizzard = blizzards[t%num_states]
		for (di, dj) in moves:
			new_pos = (i+di, j+dj)
			in_grid = 0 <= i+di <= len(grid)-1 and 0 < j+dj < len(grid[0])-1
			if new_pos in blizzard or not in_grid or grid[i+di][j+dj]:
				continue

			q.append((t+1, new_pos))



def solve(use_dfs=False):
	grid = []
	blizzard = dict()
	with open(real_file, 'r') as f:
		for i, line in enumerate(f.readlines()):
			line = line.strip()
			row = []
			for j, c in enumerate(line):
				if c in ['>', 'v', '<', '^']:
					blizzard[(i,j)] = [c]

				if c == '#':
					row.append(1)
				else:
					row.append(0)

			grid.append(row)

	M = len(grid)
	N = len(grid[0])
	all_bliz = [blizzard]
	num_states = lcm(M-2, N-2)

	blizzards = []
	for _ in range(num_states+1):
		blizzard = step(blizzard, M, N)
		blizzards.append(blizzard)

	if use_dfs:
		return dfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states)
	return bfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states)


def solve2(use_dfs=False):	
	grid = []
	blizzard = dict()
	with open(real_file, 'r') as f:
		for i, line in enumerate(f.readlines()):
			line = line.strip()
			row = []
			for j, c in enumerate(line):
				if c in ['>', 'v', '<', '^']:
					blizzard[(i,j)] = [c]

				if c == '#':
					row.append(1)
				else:
					row.append(0)

			grid.append(row)

	M = len(grid)
	N = len(grid[0])
	all_bliz = [blizzard]
	num_states = lcm(M-2, N-2)

	blizzards = []
	for _ in range(num_states+1):
		blizzard = step(blizzard, M, N)
		blizzards.append(blizzard)

	if use_dfs:
		fwd_cache = dict()
		t = dfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states, cache=fwd_cache)
		t = dfs(grid, blizzards, ((M-1), (N-2)), (0,1), num_states, t=t, cache=dict(), reverse=True)
		t = dfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states, t=t, cache=fwd_cache)
	else:
		t = bfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states)
		t = bfs(grid, blizzards, ((M-1), (N-2)), (0,1), num_states, start_time=t)
		t = bfs(grid, blizzards, (0,1), ((M-1), (N-2)), num_states, start_time=t)	
	return t



if __name__ == "__main__":
	print(solve())
	print(solve2())