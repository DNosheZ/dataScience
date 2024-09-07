F=int(input())
Robots={}
for i in range(1,F+1):Robots[i]=None
while True:
    Entrada=input().split(' ')
    if Entrada[0]=='#':break
    elif Entrada[0]=='new' and int(Entrada[1]) in Robots and int(Entrada[2]) in Robots:
        NewRobot=int(Entrada[1])+int(Entrada[2])
        while NewRobot in Robots:
            NewRobot+=1
        Robots[NewRobot]=None
    elif Entrada[0]=='search' and int(Entrada[1]) in Robots:print('existe')
    elif Entrada[0]=='search' and int(Entrada[1]) not in Robots:print('no existe')