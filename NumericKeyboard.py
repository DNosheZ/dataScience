digs=[]
while True:
    Tecla=input().split(' ')
    if Tecla[0]=='C': digs.pop()
    elif Tecla[0]=='D' and len(digs)>=int(Tecla[1]):
        for _ in range(int(Tecla[1])):digs.pop()
    elif Tecla[0]=='M' and len(digs)>=int(Tecla[2]):
        print(''.join(map(str,digs[int(Tecla[1])-1:int(Tecla[2])])))
    elif Tecla[0]=='end':break
    elif len(Tecla)==1:digs.append(int(Tecla[0]))