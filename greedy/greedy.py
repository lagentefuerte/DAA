def greedy (n, candidates):
    m = len(numeros)
    sol = [0] * m
    cont = 0
    optimal = 1
    while n >= candidates[m-1] and optimal != -1:
        optimal = getBestCandidate(n, m, candidates)
        if optimal != -1:
            n -= candidates[optimal]
            sol[optimal] += 1
            cont+=1
    return sol, cont

def getBestCandidate (n, m, candidates):
    for i in range(m):
        if candidates[i] <= n:
            return i
    return -1

n = int(input())
entrada = input()
numeros = list(map(int, entrada.split()))
candidates = sorted(numeros, reverse=True)
sol, cont = greedy(n, candidates)
print(cont)
m = len(sol)
for i in range(m):
    if sol[i] != 0:
        print(str(candidates[i]) + ": " + str(sol[i]))
