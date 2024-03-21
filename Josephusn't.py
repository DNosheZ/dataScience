import heapq
C=int(input())
for _ in range(C):
    Robin=[]
    Batman=list(map(int,input().split()))
    for i in range(Batman[0]):Robin.append(i+1)
    while len(Robin)>1:
        Robin=list(Robin)
        for capa in Robin:Robin.append((Robin.pop(0)*Batman[1])%Batman[2])
        heapq.heapify(Robin)
        for _ in range(len(Robin)//2):heapq.heappop(Robin)
    print(Robin[0])
