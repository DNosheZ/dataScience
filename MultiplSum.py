Txt=['','']
Lst=list()
while True:
    sum=0
    Txt=input().split()
    if  Txt[0]=='A':
        Lst.append(int(Txt[1]))
    elif Txt[0]=='M':
        for i in Lst:
            if i%int(Txt[1])==0: sum+=i
        print(sum)
    elif Txt[0]=='E':
        break

