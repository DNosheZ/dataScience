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

  A 1
A 2
A 3
A 4
M 1
M 2
M 3
A 5
M 6
E


10
6
3
0
