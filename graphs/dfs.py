def dfsIterative(start, visited, gAdjList):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for n in gAdjList[node]:
                if n not in visited:
                    stack.append(n)