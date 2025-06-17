from random import randint


def greedyPrim(g):
    sol = 0
    n = len(g)
    candidates = [float('inf') * n]
    initial = randint(1, n - 1)
    for (start, end, weight) in g[initial]:
        candidates[end] = weight
    visited = [False] * n
    visited[initial] = True
    for _ in range(1, n):
        (nextVertex, cost) = selectMin(visited, candidates)
        sol += cost
        visited[nextVertex] = True
        for (start, end, weight) in g[nextVertex]:
            candidates[end] = min(candidates[end], weight)
    return sol


def selectMin(visited, candidates):
    vertex = None
    weight = float('inf')
    for i in range(0, len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex = i
            weight = candidates[i]
    return vertex, weight


g = [[(0, 2, 1), (0, 3, 2), (0, 6, 6)], [(1, 5, 4), (1, 6, 7)], [(2, 0, 1), (2, 3, 3), (2, 6, 5)],
     [(3, 0, 2), (3, 2, 3), (3, 5, 9)],
     [(4, 1, 2), (4, 3, 1), (4, 6, 8)], [(5, 1, 4), (5, 3, 9)], [(6, 0, 6), (6, 1, 7), (6, 2, 5), (6, 4, 8)]]
sol = greedyPrim(g)
print(sol)
