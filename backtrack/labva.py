import copy


def labVa (lab, mejor_sol, f, c, k):
    if es_sol(lab, f, c):
        if es_mejor(lab, mejor_sol):
            mejor_sol = copy.deepcopy(lab)
    else:
        desplazamientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        lab[f][c] = k
        for desplazamiento in desplazamientos:
            if es_factible(lab, f + desplazamiento[0], c + desplazamiento[1]):
                mejor_sol = labVa(lab, mejor_sol, f + 1, c, k + 1)
        lab[f][c] = 0
    return mejor_sol

def es_sol (lab, f, c):
    return f == (len(lab) - 1) and c == (len(lab) - 1)

def es_mejor (lab, sol):
    return lab[len(lab) - 1][len(lab) - 1] < sol[len(lab) -1][len(lab) -1]

def es_factible (lab, f, c):
    return 0 <= c < len(lab) and len(lab) > f >= 0 and lab[f][c] == 0

F = 10
C = 10
lab = []
for i in range(F):
    lab.append([0] * C)
paredes = [(0, 2), (0, 7),
           (1, 0), (1, 2), (1, 5), (1, 6), (1, 8),
           (2, 6), (2, 8),
           (3, 1), (3, 4), (3, 5), (3, 6),
           (4, 2), (4, 3), (4, 7),
           (5, 5), (5, 7),
           (6, 0), (6, 3), (6, 4), (6, 7), (6, 9),
           (7, 1), (7, 2), (7, 8), (7, 9),
           (8, 2), (8, 4), (8, 5)]
for i in range(len(paredes)):
    lab[paredes[i][0]][paredes[i][1]] = float('inf')
sol_ini = [[float('inf')] for _ in range(C)] * F
print(labVa(lab, sol_ini, 0, 0, 0))
