Fila=[]
while True:
    Persona=input().split()
    if Persona==['0','0']: print(len(Fila)); break
    Persona[1]=int(Persona[1])
    if len(Fila)<Persona[1]: Fila.append(Persona)
    for P in Fila:
        if len(Fila)>P[1]:Fila.pop(Fila.index(P))

A 1
B 2
C 2
D 3
0 0

2
