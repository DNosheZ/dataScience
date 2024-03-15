Lst=[]
while True:
    Type=input().split()
    if Type[0]=='end': break
    elif len(Type)==1 and Type[0] not in ['end','C']: Lst.append(int(Type[0])
    elif len(Lst)!=0 and Type[0]=='C': Lst.pop()
    elif Type[0]=='D' and len(Lst)-int(Type[1])>=0: Lst=Lst[:-int(Type[1])]                                                                                                                                                                                                                                         )
    elif Type[0]=='M' and (0<=int(Type[1])<=len(Lst)) and 0<=int(Type[2])<=len(Lst):
        print(''.join(map(str,Lst[int(Type[1])-1:int(Type[2])])))
