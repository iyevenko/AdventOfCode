def solve(f):
    edges = {}
    for line in open(f).read().splitlines():
        n1, n2 = line.split('-')
        if n1 in edges:
            edges[n1].append(n2)
        else:
            edges[n1] = [n2]
        
        if n2 in edges:
            edges[n2].append(n1)
        else:
            edges[n2] = [n1]


    def dfs(node, visited):
        s = 0
        for node2 in edges[node]:
            if node2 in visited or node2 == 'start':
                continue
            if node2 == 'end':
                s += 1
                continue

            new_visited = visited | {node2} if node2.islower() else visited
            s += dfs(node2, new_visited)
        return s

    return dfs('start', set())


def solve2(f):
    edges = {}
    for line in open(f).read().splitlines():
        n1, n2 = line.split('-')
        if n1 in edges:
            edges[n1].append(n2)
        else:
            edges[n1] = [n2]
        
        if n2 in edges:
            edges[n2].append(n1)
        else:
            edges[n2] = [n1]


    def dfs(node, visited, maxed_visit):
        s = 0
        for node2 in edges[node]:
            if node2 == 'start':
                continue
            if node2 == 'end':
                s += 1
                continue
            if node2.isupper():
                temp_visited = visited.copy()
                temp_visited[node2] = temp_visited.get(node2, 0) + 1
                s += dfs(node2, temp_visited, maxed_visit)
                continue

            n_visits = visited.get(node2, 0)
            temp_visited = visited.copy()
            if n_visits == 0:
                temp_visited[node2] = 1
                s += dfs(node2, temp_visited, maxed_visit)
            elif n_visits == 1 and not maxed_visit:
                temp_visited[node2] = 2
                s += dfs(node2, temp_visited, True)
        return s

    return dfs('start', {}, False)
    

if __name__ == '__main__':
    # print(solve('12_test.txt'))
    print(solve('12.txt'))
    # print(solve2('12_test.txt'))
    print(solve2('12.txt'))
