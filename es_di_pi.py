import heapq
Duracion=int(input())
Inits=[]
C=int(input())
Track=0
Star=[]
heapq.heapify(Star)
for _ in range(C):
    T=list(map(int,input().split()))
    Inits.append(T[1:])
    heapq.heappush(Star,T[1])
heapq.heapify(Inits)
while Track<=Duracion:
    Baki=sum(1 for Tono in Inits if (Track%Tono[1]==0 and Track>=Tono[0] and Track!=0))
    if len(Star)>0 and Track==Star[0]:print(Track);heapq.heappop(Star)
    for _ in range(Baki):print(Track)
    Track+=1
#cada tono suena cada b milisegundos despues de su momento de inicio
#momento de inicio del tono + b_milisegundos
