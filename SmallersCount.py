from collections import Counter
for _ in range(int(input())):
    nums = map(int, input().split())
    conteos = Counter(nums)
    elementos_ordenados = sorted(conteos.items())
    conteos_ordenados = [str(conteo) for _, conteo in elementos_ordenados]
    print(' '.join(conteos_ordenados))
