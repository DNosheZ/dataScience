from collections import deque
Uroboros=deque()
MsgEv=[str,str]
while MsgEv[0]!="termina":
    MsgEv=[input().split()]
    if MsgEv[0]=='agrega':
        Uroboros.append(MsgEv[1])
    elif MsgEv[0]=='engulle':
        if Uroboros[0]>Uroboros[1]:
            Uroboros.pop()
        elif Uroboros[0]<=Uroboros[-1]:
            Uroboros.popleft()
    elif MsgEv[0]=='termina':
        if len(Uroboros)==0:
            print('uroboro vacio')    
        else:
            print(f'cabeza {Uroboros[0]} cola {Uroboros[-1]}')    

agrega 10
agrega 15
engulle
agrega 7
agrega 4
engulle
agrega 15
engulle
agrega 8
termina

cabeza 7 cola 8
