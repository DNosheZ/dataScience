def criba_eratostenes(max_n):
    es_primo = [True] * (max_n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for i in range(2, int(max_n**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, max_n + 1, i):
                es_primo[j] = False

    primos = [i for i in range(2, max_n + 1) if es_primo[i]]
    return primos, es_primo

def contar_parejas_primos(N, primos, es_primo):
    contador = 0
    for p in primos:
        if p > N // 2:
            break
        if es_primo[N - p]:
            contador += 1
    return contador

def main():
    max_n = 10000
    primos, es_primo = criba_eratostenes(max_n)
    
    C = int(input())
    resultados = []
    
    for _ in range(C):
        N = int(input())
        if N % 2 == 0 and N >= 4:
            contador = contar_parejas_primos(N, primos, es_primo)
            resultados.append(str(contador))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()
