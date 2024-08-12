from collections import deque
for _ in range(int(input())):
    x=int(input())#revisar
    A_bar=deque([i for i in range(1, x+1)])
    B_bar=deque()
    C_bar=deque()
    h=0
    while True:
        A,B=map(str,input().split(' '))
        if A=='X' and B=="X":
            if h>0:
                print('secuencia invalida')
                break
            elif C_bar!=deque([j for j in range(1,x+1)]):
                print('no soluciona la torre')
            
            else:print('soluciona la torre')
            break
        elif A!=B:
            if A=='A' and B=='B':
                if len(A_bar)==0 or (len(B_bar)>0 and A_bar[0]>=B_bar[0]):
                    h+=1
                else:B_bar.appendleft(A_bar.popleft())
            elif A=='A' and B=='C':
                if len(A_bar)==0 or (len(C_bar)>0 and A_bar[0]>=C_bar[0]):
                    h+=1
                else:C_bar.appendleft(A_bar.popleft())
            elif A=='B' and B=='A':
                if len(B_bar)==0 or (len(A_bar)>0 and B_bar[0]>=A_bar[0]):
                    h+=1
                else:A_bar.appendleft(B_bar.popleft())
            elif A=='B' and B=='C':
                if len(B_bar)==0 or (len(C_bar)>0 and B_bar[0]>=C_bar[0]):
                    h+=1
                else:C_bar.appendleft(B_bar.popleft())
            elif A=='C' and B=='A':
                if len(C_bar)==0 or (len(A_bar)>0 and C_bar[0]>=A_bar[0]):
                    h+=1
                else:A_bar.appendleft(C_bar.popleft())
            elif A=='C' and B=='B':
                if len(C_bar)==0 or (len(B_bar)>0 and C_bar[0]>=B_bar[0]):
                    h+=1
                else:B_bar.appendleft(C_bar.popleft())
        else: continue