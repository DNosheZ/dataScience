# Leer N y T
N, T = map(int, input().split())

# Leer los elementos del arreglo
A = [int(input()) for _ in range(N)]

# Ordenar el arreglo para simplificar la búsqueda de ternas ordenadas
A.sort()

# Lista para almacenar las ternas encontradas
ternas = []

# Buscar las ternas que suman T
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] == T:
                ternas.append((A[i], A[j], A[k]))

# Verificar si se encontraron ternas
if ternas:
    # Imprimir cada terna en orden ascendente
    for terna in ternas:
        print(*terna)
else:
    # Mostrar mensaje si no hay ternas que cumplan la condición
    print('No hay trillizas')
