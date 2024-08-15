for _ in range(int(input())):
    Lst=[]
    instruccion1,instruccion2=map(int,input().split(' '))
    for i in range(instruccion1):Lst.append(i+1)
    k=instruccion2
    while True:
        if len(Lst)==1:break
        Bye=Lst[k-1]
        Lst=Lst[k:]+Lst[0:k-1]
        Div=len(Lst)
        k=Bye%Div
        if k==0:k=1
    print(Lst[0])
