def greedyKruskal(g):
    sol = 0
    candidates = sortCandidates(g)
    components = list(range(len(g)))
    numComponents = len(components)
    i = 0
    while i < len(candidates) and numComponents > 1:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            sol += weight
            numComponents -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return sol


def updateComponents (components, newID, oldID):
    for i in range(len(components)):
        if components[i] == oldID:
            components[i] = newID



def sortCandidates(g):
    candidates = []
    for i in range(len(g)):
        for (end, weight) in g[i]:
            candidates.append((weight, i, end))
    candidates.sort()
    return candidates


g = [[(2, 1), (3, 2), (6, 6)], [(5, 4), (6, 7)], [(0, 1), (3, 3), (6, 5)], [(0, 2), (2, 3), (5, 9)],
     [(1, 2), (3, 1), (6, 8)], [(1, 4), (3, 9)], [(0, 6), (1, 7), (2, 5), (4, 8)]]
sol = greedyKruskal(g)
print(sol)
