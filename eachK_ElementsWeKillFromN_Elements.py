C=int(input())
for _ in range(C):
    MD=list(map(int,input().split()))
    Lst=[i for i in range(1,MD[0]+1)]
    k=MD[1]#k indicara la cantidad de saltos hasta llegar al estudiante a eliminar
    Partida=0#indice
    while len(Lst)>1:
        Sal=Lst[Partida+k-1]#estudiante que sera eliminado
        if Sal==Lst[-1]: Partida=0#indice del estudiante que sucede al eliminado
        else: Partida=Lst.index(k)#indice
        Lst.pop(Sal)#eliminamos a ese estudiante de la lista
        k=k%Lst[Partida]#cantidad de indices a saltar para hallar el estudiante a eliminar
        if Partida+k>len(Lst):#correjimos k, en caso que la posicion sobrepase las dedicadas a la lista, recien organizada
            AL=Lst.index(Lst[-1])
            k-=AL
            Partida=0
        if k==0 or len(Lst)==1:
            print(Lst[0])
            break
            
        

3
5 3
10 7
99 11

5
3
12
