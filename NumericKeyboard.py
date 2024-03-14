Lst=[]
while True:
    sum=0
    Type=input().split()
    if Type[0]=='end': break
    elif len(Type)==1 and (Type[0]!='C' or Type[0]!='end'): Lst.append(int(Type[0])
    elif len(Lst)!=0 and Type[0]=='C': Lst.pop()
    elif Type[0]=='D' and len(Lst)-int(Type[1])>=0:
        for _ in range(int(Type[1])): Lst.pop()                                                                                                                                                                                                                                          )
    elif len(Type)==3 and int(Type[1])<=len(Lst) and int(Type[2])<=len(Lst):
        for i in range(int(Type[1]),int(Type[2])+1):
                    sum+=Lst[i-1]
                    if i==int(Type[1]) or i!=int(Type[2]):#solo multiplicamos por 10, para sumarle, cuando es el primer elemento a sumar
                        sum*=10
                    else:
                        break
        print(sum)
