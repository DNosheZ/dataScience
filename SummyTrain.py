import heapq
c = int(input())
for _ in range(c):
    X=[]
    Y=[]
    n=int(input())
    tren=list(map(int,input().split()))
    while True:
        heapq.heapify(tren)
        if len(tren) == 0:
          firt = int("".join(map(str,Y)))
          second = int("".join(map(str,X)))
          print(firt+second)
          break
        if len(tren)%2 == 0:
            X.append(heapq.heappop(tren))
        else:
            Y.append(heapq.heappop(tren))
