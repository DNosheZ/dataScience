from collections import deque
Cilinder=deque()
for _ in range(int(input())):
    Line=list(map(int,input().split(' ')))
    Del=0
    if Line[0]==1 and Line[2]!=0:
        for _ in range(Line[2]):Cilinder.append(Line[1])
    elif Line[0]==2 and Line[1]!=0 and len(Cilinder)>=int(Line[1]):
        for _ in range(int(Line[1])):Del+=Cilinder.popleft()
        print(Del)
Cilinder2=()
for _ in range(int(input())):
    Line2=list(map(int,input().split(' ')))
    if Line2[0]==1 and Line2[2]!=0:
        Cilinder2+=tuple([])
    elif Line2[0]==2 and Line2[1]!=0 and len(Cilinder2)>=int(Line2[1]):
        Del2=sum(Cilinder2[0:Line[1]])
        Cilinder2=Cilinder2[Line[1]: ]
        print(Del2)