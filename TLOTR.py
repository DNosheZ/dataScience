from collections import deque
for _ in range(int(input())):
    A=list(map(int, input().split()))
    B=deque()
    for i in A: B.appendleft(i)

    while True:
        if len(B)>1 and (B[0]+B[1])%2==0:
            D=B.popleft()
            E=B.popleft()
            B.appendleft((D+E)//2)
        else:break
    print(f'{len(B)} {B[0]}')