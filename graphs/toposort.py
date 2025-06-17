def toposort(g, order_index):
    n = len(g)
    entry_degrees = [0] * n
    start = deque()
    visited = set()
    for node in g:
        for end in node:
            entry_degrees[end] += 1
    for i in range(len(entry_degrees)):
        if entry_degrees[i] == 0:
            start.append(i)
    start = deque(sorted(start, key=lambda x: order_index[x]))
    order = []
    while start:
        current = start.popleft()
        visited.add(current)
        order.append(current)
        for end in g[current]:
            entry_degrees[end] -= 1
        for i in range(len(entry_degrees)):
            if entry_degrees[i] == 0 and i not in visited:
                start.append(i)
                start = deque(sorted(start, key=lambda x: order_index[x]))
    return order