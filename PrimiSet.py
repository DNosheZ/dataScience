from collections import Counter
for _ in range(int(input())):
  LstRq=[int(x) for x in input().split()]
  N, P=LstRq[0], LstRq[1]
  LstPrv=[int(y) for y in input().split()]
  LstDv=[]
  for i in range(1,P+1):
    if P%i==0:
      LstDv.append(i)
  if all(el in LstPrv for el in LstDv):
    print('Es Primiconjunto')
  else:
    print('No es Primiconjunto')    

2
6 10
1 2 3 4 5 10
4 21
1 3 8 21


Es Primiconjunto
No es Primiconjunto

  
