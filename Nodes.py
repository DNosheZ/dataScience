from collections import deque

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.visitado = False
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)


def dfs(grafo, nodo_inicial):
    # Marcamos todos los nodos como no visitados
    for nodo in grafo:
        nodo.visitado = False

    # Creamos una pila y agregamos el nodo inicial
    pila = []
    pila.append(nodo_inicial)

    # Mientras la pila no esté vacía
    while pila:
        nodo_actual = pila.pop()
        if not nodo_actual.visitado:
            # Marcamos el nodo como visitado
            nodo_actual.visitado = True
            print(f"Nodo visitado: {nodo_actual.nombre}")

            # Añadimos a la pila los vecinos no visitados
            for vecino in nodo_actual.vecinos:
                if not vecino.visitado:
                    pila.append(vecino)


def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].visited = True
                print(b)
                q.append(b)

def minimal_hops(grafo, nodo_inicial):
    # Marcamos todos los nodos como no visitados
    for nodo in grafo:
        nodo.visitado = False
        nodo.hops = None

    # Marcamos el nodo inicial
    nodo_inicial.visitado = True
    nodo_inicial.hops = 0
    q = deque()
    q.append(nodo_inicial)

    while q:
        nodo_actual = q.popleft()
        print(f"Nodo: {nodo_actual.nombre}, Hops: {nodo_actual.hops}")

        for vecino in nodo_actual.vecinos:
            if not vecino.visitado:
                vecino.visitado = True
                vecino.hops = nodo_actual.hops + 1
                q.append(vecino)

def connectedComponents(grafo):
    # Inicializamos el contador de componentes conectados
    contador_componentes = 0
    
    for nodo in grafo:
        if not nodo.visitado:
            # Encontramos un nuevo componente conectado
            contador_componentes += 1
            # Realizamos un recorrido en profundidad (DFS) para marcar todos los nodos en este componente
            s = []
            s.append(nodo)
            while s:
                u = s.pop()
                if not u.visitado:
                    u.visitado = True
                    for vecino in u.vecinos:
                        if not vecino.visitado:
                            s.append(vecino)

    return contador_componentes#devuelve la cantidad de subgrafos

def crear_grafo(P, entradas):
    nodos = [Nodo(i) for i in range(P)]

    for i, entrada in enumerate(entradas):
        nodos[i].nombre = i
        vecinos = entrada.split()  # Dividir el string en números (strings)
        for vecino in vecinos:
            vecino = int(vecino)  # Convertir el string a entero
            if 0 <= vecino < P:
                nodos[i].agregar_vecino(nodos[vecino])
    
    return nodos


# # Ejemplo de uso
# # Creación de nodos
# nodo_a = Nodo('A')
# nodo_b = Nodo('B')
# nodo_c = Nodo('C')
# nodo_d = Nodo('D')
# nodo_e = Nodo('E')
# nodo_f = Nodo('F')

# # Creación de conexiones (aristas)
# nodo_a.agregar_vecino(nodo_b)
# nodo_b.agregar_vecino(nodo_a)
# nodo_a.agregar_vecino(nodo_c)
# nodo_c.agregar_vecino(nodo_a)
# nodo_d.agregar_vecino(nodo_e)
# nodo_e.agregar_vecino(nodo_d)
# nodo_e.agregar_vecino(nodo_f)
# nodo_f.agregar_vecino(nodo_e)
# nodo_a.agregar_vecino(nodo_f)
# nodo_f.agregar_vecino(nodo_a)

# # Creación del grafo
# grafo = [nodo_a, nodo_b, nodo_c, nodo_d, nodo_e, nodo_f]

# # Contar los componentes conectados
# num_componentes = connectedComponents(grafo)
# print(f"Número de componentes conectados: {num_componentes}")

# #Paulina ball
# for _ in range(int(input())):
#     Entrada=list(map(int,input().split('; ')))
#     for _ in range(Entrada[1]):
#         Dancers=list(map(int,input().split(' ')))


#Chismes
P=int(input())
entradas=[]
for i in range(P):
    entradas.append(input())
grafo=crear_grafo(P,entradas)

    


    

