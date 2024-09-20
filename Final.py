N,Q=list(map(int,input().split()))
Entrada=list(map(int,input().split()))
Eventos={}
if len(Entrada)==N:
    for i in Entrada:
        if i not in Eventos.keys():
            Eventos[i]=1
        else:Eventos[i]+=1
    for _ in range(Q):
        Pregunta=list(map(int,input().split()))
        if Pregunta[0] in Eventos.keys() and Eventos[Pregunta[0]]>=Pregunta[1]:print('SI')
        else:print('NO')