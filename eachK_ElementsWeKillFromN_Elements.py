N=int(input())
for _ in range(N):
    circulo=[]
    Caso=list(map(int,input().split()))
    k=Caso[1]
    for i in range(Caso[0]): circulo[i]=i+1
    f=0
    while True:
        if len(circulo)==1:
            print(circulo[0])
            break
        elif (circulo.index(f)+k-1 not in range(len(circulo))):
            eliminado=circulo.index(f)+k-1-len(circulo)
            f=circulo[eliminado+1]
            circulo.pop(eliminado)
            k%=f
        elif circulo.index(f)+k-1<=len(circulo):
            eliminado=circulo.index(f)+k-1
            f=circulo[eliminado+1]
            circulo.pop(eliminado)
            k%=f
