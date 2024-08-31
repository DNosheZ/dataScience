Winners={}
G=0
M=int(input())
while True:
    Entrada=input().split(' ')
    if Entrada[0]=='end':break
    elif Entrada[0]=='sms' and Entrada[1] in Winners:
        Winners[Entrada[1]]+=1
        print(f"{Entrada[1]} {M//(Winners[Entrada[1]]*G)}")

    elif Entrada[0]=='winner' and Entrada[1] not in Winners:
        Winners[Entrada[1]]=0
        G+=1
