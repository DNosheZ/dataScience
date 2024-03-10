Lst=[]
while True:
    sum=0
    Type=input().split()
    if len(Type)==1:
        if Type[0]=='end':
            break
        elif Type[0]=='C':
            if len(Lst)>0:Lst.pop()#imposible eliminar elementos de una lista vacia
            else:continue
        else:Lst.append(int(Type[0]))
    elif len(Type)==2:
        if int(Type[1])>len(Lst):continue#si se pide que se borren mas numeros de los que hay en la lista, paila siguiente instruccion
        else:
            for _ in range(int(Type[1])):Lst.pop()
    elif len(Type)==3:
        if int(Type[1])>len(Lst) or int(Type[2])>len(Lst):continue#no se pueden mostrar mas numeros de los que ya hay en la lista
        else:
            if int(Type[1])==int(Type[2]):
                print(Lst[int(Type[1])-1])
            else:
                for i in range(int(Type[1]),int(Type[2])+1):
                    sum+=Lst[i-1]
                    if i==int(Type[1]) or i!=int(Type[2]):#solo multiplicamos por 10, para sumarle, cuando es el primer elemento a sumar
                        sum*=10
                    else:
                        break
            print(sum)
    else:continue#si no se entendio la instruccion, seguimos el programa hasta el end

9
8
7
M 1 1
C
6
D 4
5
D 1
4
M 3 5
M 2 4
end
