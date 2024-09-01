Votos={}
Final={}
while True:
    Entrada=list(map(int,input().split(' ')))
    if Entrada==[0,0]:
        for x in Votos.values():
            if x[1] in Final and x[0]==1:Final[x[1]][1]+=1
            elif x[1] not in Final and x[0]==1:Final[x[1]]=[x[1],1]
        Final=dict(sorted(Final.items(),
                          key=lambda item: (-item[1][1] if list(Final.values()).count(item[1]) == 1 
                                            else -item[1][0], -item[1][0])))
        for x in Final.values():print(f'{x[0]} {x[1]}')
        break
    if Entrada[0] in Votos:Votos[Entrada[0]][0]+=1
    else: Votos[Entrada[0]]=[1,Entrada[1]]
