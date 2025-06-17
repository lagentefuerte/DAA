def selectMinDistance(distances, visited):
    minDistance = float('inf')
    bestItem = None

    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDistance:
            minDistance = distances[i]
            bestItem = i

    return bestItem


def greedyDijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for (end,weight) in g[origin]:
        distances[end] = weight

    for _ in range(1,n):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for (end,weight) in g[nextNode]:
            new_distance = distances[nextNode] + weight
            if new_distance < distances[end]:
                distances[end] = new_distance

    return distances

n, m = map(int, input().strip().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    (start, end, weight) = map(int, input().strip().split())
    adjList[start].append((end, weight))
    adjList[end].append((start, weight))
max_cost = 0
for i in range(n):
    distances = greedyDijkstra(adjList, i)
    for distance in distances:
        if distance > max_cost:
            max_cost = distance
print(max_cost)