from collections import deque
C=int(input())
for _ in range(C):
    N,k = map(int,input().split())
    Rq=deque(map(int,input().split()))
    Elfo=deque([1]*N)
    Elfo[k-1]=2
    Time=0
    activo=True
    while activo:
        if Rq[0]==0:
            if Elfo[0]==2:
                print(Time)
                activo=False
                break
            Rq.popleft()
            Elfo.popleft()
        Rq[0]-=1
        Rq.append(Rq.popleft())
        Elfo.append(Elfo.popleft())
        Time+=5
        


  2
5 5
1 2 3 4 5
5 3
1 2 3 4 5


75
50
