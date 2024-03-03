from collections import deque
rev=[')',']','}']
for _ in range(int(input())):
    exp=deque(input().split())
    if exp[-1]!=';':
        print('incorrecta')
        continue
    exp.pop()#eliminamos la coma, para facilitar la vida
    while exp:
        cont1=exp[0]
        cont2=exp[-1]
        cont3=exp[1]
        if cont1=='(':#se revisa que se halla abierto con parentesis
            if cont2!=rev[0] and cont3!=rev[0]:
                print('incorrecta')
                break
            else:
                if cont2==rev[0]: exp.pop(), exp.popleft()
                elif  cont3==rev[0]: 
                    for i in range(2): exp.popleft()
                continue

        elif cont1=='[':#o con corchete
            if cont2!=rev[1] and cont3!=rev[1]:
                print('incorrecta')
                break
            else:
                if cont2==rev[1]: exp.pop(), exp.popleft()
                elif  cont3==rev[1]: 
                    for i in range(2): exp.popleft()
                continue

        elif cont1=='{':#o con llave
            if cont2!=rev[2] and cont3!=rev[2]:
                print('incorrecta')
                break
            else:
                if cont2==rev[2]: exp.pop(), exp.popleft()
                elif  cont3==rev[2]: 
                    for i in range(2): exp.popleft()
                continue

        else:
            print('incorrecta')
            break
    if  not exp:print("correcta")
    continue

3
{ [ ( ) ] } ;
[ ] { } ( ) ;
( ) { [ } ] ;


correcta
correcta
incorrecta
