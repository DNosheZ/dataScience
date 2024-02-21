def calcular_saltos(N, tablero):
    visitado = [False] * N  # Para llevar un registro de las casillas visitadas
    saltos = 0
    casilla_actual = 0

    while casilla_actual >= 0 and casilla_actual < N and not visitado[casilla_actual]:
        visitado[casilla_actual] = True
        casilla_actual += tablero[casilla_actual]
        saltos += 1

    return saltos

def main():
    casos = int(input())
    
    for _ in range(casos):
        N = int(input())
        tablero = list(map(int, input().split()))
        
        saltos = calcular_saltos(N, tablero)
        print(saltos)

if __name__ == "__main__":
    main()
