from collections import deque
Lst1= tuple(map(int, input().split()))
LstReSellers=deque()
disponibles=Lst1[1]
h=0
for _ in range(Lst1[0]):
    Sell=tuple(map(int,input().split()))
    LstReSellers.append(Sell)
while disponibles>0 and len(LstReSellers)>0:
    i=LstReSellers[0]
    if disponibles<=i[1]:#al haber menos boletas de las solicitadas por el cliente, acabamos
        print(f'{i[0]} {disponibles}')
        break
    disponibles-=i[1]#se van suprimiendo de las boletas disponibles, las solicitadas por el comprador
    h+=1
    LstReSellers.popleft()
    if h%5!=0:
        LstReSellers.append(i)
if len(LstReSellers)>0 and disponibles!=0:
    print('quedaron boletas disponibles')
