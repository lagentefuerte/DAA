import copy

def inicializarDatos():
    N, P, B = map(int, input().strip().split())
    datos = {}
    datos['N'] = N
    datos['W'] = P
    datos['B'] = B
    datos['Nombre'] = []
    datos['Peso'] = []
    datos['Valor'] = []
    for i in range(datos['N']):
        O, C, G = input().strip().split()
        datos['Nombre'].append(O)
        datos['Peso'].append(int(C))
        datos['Valor'].append(int(G))
    return datos


def inicializarSolucion(datos):
    sol = {}
    sol['PesoAc'] = 0
    sol['ValorAc'] = 0
    sol['Objetos'] = [0] * datos['N']
    return sol

def mejor(mejorSol, sol):
    if sol['ValorAc'] > mejorSol['ValorAc']:
        return copy.deepcopy(sol)
    return mejorSol

def esSolucion(sol, datos):
    return sol['PesoAc'] + min(datos['Peso']) > datos['W']

def esFactible(sol, datos, i):
    return sol['PesoAc'] + datos['Peso'][i] <= datos['W']

def asignar(sol, i, datos):
    sol['PesoAc'] += datos['Peso'][i]
    sol['ValorAc'] += datos['Valor'][i]
    sol['Objetos'][i] += 1
    return sol

def borrar(sol, i, datos):
    sol['PesoAc'] -= datos['Peso'][i]
    sol['ValorAc'] -= datos['Valor'][i]
    sol['Objetos'][i] -= 1
    return sol

def noMasObjetos(datos, k):
    return datos['N'] <= k

def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos) or noMasObjetos(datos, k):
        mejorSol = mejor(mejorSol, sol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol, datos, i):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i + 1)
                sol = borrar(sol, i, datos)
    return mejorSol


datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
nombres = [datos['Nombre'][i] for i in range(datos['N']) if mejorSol['Objetos'][i] == 1]
nombres.sort(key=str.lower)
print(*nombres)
print(str(mejorSol['PesoAc']) + " " + str(mejorSol['ValorAc']))
print("SE VA" if mejorSol['ValorAc'] > datos['B'] else "VUELVE")
