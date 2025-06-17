import heapq
import copy

cost_matrix = [
    [11,12,18,40],
    [14,15,13,22],
    [11,17,19,23],
    [17,14,20,28]
]
n = len(cost_matrix[0])

def isSol (node_u, n):
    return node_u[0] == n-1

def initSol (W, arr, n):
    sol = []
    act_weight = 0
    sorted(arr, reverse=True, key=lambda x: x[0]/x[1])



def jobAsignBaB (W, arr, n):
    arr.sort(reverse=True)
    node_u = (-1, 0, 0, 0) # nivel, profit, cota, peso
    q = []
    heapq.heappush(q, node_u)
    max_profit = 0
    while q:
        node_u = heapq.heappop(q)
        if isSol(node_u, n):
            if node_u[1] > max_profit:
                max_profit = node_u[1]
        else:
            if node_u[1] >= lowerbound(XXX):
                childs = complete(sol, cost_matrix)
                for child in childs:
                    heapq.heappush(q, child)
    return finalSol

def complete (sol, cost_matrix):
    childs = []
    level = len(sol[1])
    _, current_assign, a = sol
    for job in range(n):
        if job not in current_assign:
            child = copy.deepcopy(sol[1])
            child.append(job)
            new_cost = sol[0] + cost_matrix[level][job]
            lb = lowerbound((new_cost, child), cost_matrix)
            childs.append((new_cost, child, lb))
    return childs

def lowerbound (sol, cost_matrix):
    bound = sol[0]
    for e in range(len(sol[1]), len(cost_matrix)):
        min_cost = float('inf')
        for i in range(len(cost_matrix)):
            min_cost = min(min_cost, cost_matrix[e][i])
        bound += min_cost
    return bound

finalSol = jobAsignBaB(cost_matrix)
print(finalSol)

