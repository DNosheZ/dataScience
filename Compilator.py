from collections import deque
rev1=[')',']','}']
rev2=['(','[','{']
for _ in range(int(input())):
    exp=deque(input().split())
    exp2=deque()
    if exp[-1]!=';':
        print('incorrecta')
        continue
    exp.pop()#eliminamos la coma, para facilitar la vida
    while exp:
        if exp[0] in rev1:
            if exp[0]==')': bop=rev2[0]
            elif exp[0]==']': bop=rev2[1]
            elif exp[0]=='}': bop=rev2[2]
            if exp2[-1] !=bop:  
                print('incorrecta')
                break
            else:
                exp.popleft()
                exp2.pop()
                
        else:#
            exp2.append(exp.popleft())
    if  len(exp)==0 or len(exp2)==0 : print('correcta')
    continue
