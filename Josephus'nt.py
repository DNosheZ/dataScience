import heapq
C=int(input())
for _ in range(C):
    Robin=[]
    Batman=list(map(int,input().split()))
    #sera necesaria comprobar si A y B son primos?
    #en caso que si, si no son primos ambos, se pasara al siguiente caso, y de la contrario, se seguira revisando el caso actual
    #A=Batman[1]; B=Batman[2]
    for i in range(Batman[0]):Robin[i]=i+1
    while True:
        for capa in Robin:capa=(capa*Batman[1])%Batman[2]
        heapq.heapify(Robin)
        if len(Robin)==1:print(Robin[0]);break
        for _ in range(len(Robin)//2):heapq.heappop(Robin)
