from collections import deque


def bfs(gAdjList):
    visited = set()
    cont = 0
    for v in range(len(gAdjList)):
        if v not in visited:
            cont += 1
            bfs_aux(gAdjList, visited, v)
    return cont


def bfs_aux(gAdjList, visited, v):
    queue = deque()
    queue.append(v)
    visited.add(v) 
    while queue:
        v = queue.popleft()
        for node in gAdjList[v]:
            if node not in visited:
                visited.add(node)
                queue.append(node)


n, m = map(int, input().strip().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    v1, v2 = map(int, input().strip().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

print(bfs(adjList))