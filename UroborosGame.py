from collections import deque
Uroboros=deque()
while True:
    entrada = input().split()
    operacion = entrada[0]
    if operacion=='agrega':
        Uroboros.append(int(entrada[1]))
    elif operacion=='engulle':
        if Uroboros[0]>Uroboros[-1]:
            Uroboros.pop()
        elif Uroboros[0]<=Uroboros[-1]:
            Uroboros.popleft()
    elif operacion=='termina':
        if len(Uroboros)==0:
            print('uroboro vacio')    
        else:
            print(f'cabeza {Uroboros[0]} cola {Uroboros[-1]}')    
        break
