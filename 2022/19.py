test_file = '19_test.txt'
real_file = '19.txt'

import re
from math import ceil
import math

mats = ['ore', 'clay', 'obsidian', 'geode']


def step(t, T, costs, target, robots, supply):
	dts = [ceil((costs[target][i] - supply[m])/robots[m]) for i, m in enumerate(mats) if costs[target][i] > supply[m]]
	dt = max(dts) if dts else 0
	dt = min(dt, T-t)
	# print(dt)
	supply = {k: v + dt*robots[k] for (k, v) in supply.items()}
	t += dt
	if t >= T:
		return t, robots, supply

	supply = {m: supply[m] - costs[target][i] for i, m in enumerate(mats)}
	supply = {k: v + robots[k] for (k, v) in supply.items()}
	robots[target] += 1
	t += 1
	return t, robots, supply


def dfs(costs, max_costs, t=0, T=24, robots=None, supply=None, cache=None, best=0):
	if t >= T:
		return supply['geode']

	# If making a geode robot every turn isn't enough
	n = T-t
	if n*(n+1)/2 + n*robots['geode'] < best-robots['geode']-supply['geode']:
		return 0

	supply = {k: min(v, n*max_costs[k]) for k, v in supply.items()}

	state = (t, *robots.values(), *supply.values())
	if state in cache:
		return cache[state]

	for target in mats[::-1]:
		if any(robots[m] == 0 for i, m in enumerate(mats) if costs[target][i]):
			continue
		target_idx = mats.index(target)

		if robots[target] >= max_costs[target]:
			continue
		new_t, new_robots, new_supply = step(t, T, costs, target, robots.copy(), supply.copy())
		best = max(best, dfs(costs, max_costs, new_t, T, new_robots, new_supply, cache, best))

	cache[state] = best
	return best



def solve():
	blueprints = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			blueprint = list(map(int, re.findall(r'[0-9]+', line)))
			blueprints.append(blueprint)

	score = 0
	for blueprint in blueprints:
		idx, ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs = blueprint
		costs = {
			'ore': [ore_cost, 0, 0, 0],
			'clay': [clay_cost, 0, 0, 0],
			'obsidian': [obs_cost_ore, obs_cost_clay, 0, 0],
			'geode': [geode_cost_ore, 0, geode_cost_obs, 0]
		}
		robots = {
			'ore': 1,
			'clay': 0,
			'obsidian': 0,
			'geode': 0
		}
		supply = {
			'ore': 0,
			'clay': 0,
			'obsidian': 0,
			'geode': 0
		}
		max_costs = {
			'ore': max(c[0] for c in costs.values()),
			'clay': obs_cost_clay,
			'obsidian': geode_cost_obs,
			'geode': math.inf
		}

		geodes = dfs(costs, max_costs, robots=robots, supply=supply, cache=dict())
		score += idx * geodes

	return score

def solve2():
	blueprints = []
	with open(real_file, 'r') as f:
		for line in f.readlines():
			blueprint = list(map(int, re.findall(r'[0-9]+', line)))
			blueprints.append(blueprint)

	score = 1
	for blueprint in blueprints[:3]:
		idx, ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs = blueprint
		costs = {
			'ore': [ore_cost, 0, 0, 0],
			'clay': [clay_cost, 0, 0, 0],
			'obsidian': [obs_cost_ore, obs_cost_clay, 0, 0],
			'geode': [geode_cost_ore, 0, geode_cost_obs, 0]
		}
		robots = {
			'ore': 1,
			'clay': 0,
			'obsidian': 0,
			'geode': 0
		}
		supply = {
			'ore': 0,
			'clay': 0,
			'obsidian': 0,
			'geode': 0
		}
		max_costs = {
			'ore': max(c[0] for c in costs.values()),
			'clay': obs_cost_clay,
			'obsidian': geode_cost_obs,
			'geode': math.inf
		}

		geodes = dfs(costs, max_costs, T=32, robots=robots, supply=supply, cache=dict())
		score *= geodes

	return score


if __name__ == "__main__":
	print(solve())
	print(solve2())