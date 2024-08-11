from collections import deque
for _ in range(int(input())):
    x=int(input())
    A,B=['','']
    A_bar=deque([i for i in range(1, x+1)])
    B_bar=deque()
    C_bar=deque()
    while True:
        if C_bar==deque([k for k in range(1, x+1)]):
            print('soluciona la torre')
            break
        A,B=map(str,input().split(' '))
        if A=='X' and B=="X":
            if C_bar!=deque([j for j in range(1,x+1)]):
                print('no soluciona la torre')
            break
        elif A!=B:
            if A=='A' and B=='B':
                Entrega=A_bar
                Recibe=B_bar
            elif A=='A' and B=='C':
                Entrega=A_bar
                Recibe=C_bar
            elif A=='B' and B=='A':
                Entrega=B_bar
                Recibe=A_bar
            elif A=='B' and B=='C':
                Entrega=B_bar
                Recibe=C_bar
            elif A=='C' and B=='A':
                Entrega=C_bar
                Recibe=A_bar
            elif A=='C' and B=='B':
                Entrega=C_bar
                Recibe=B_bar
            if Entrega[0]>=Recibe[0]:
                print('secuencia invalida')
                break
            else: Recibe.appendleft(Entrega.popleft())
        else: continue
        