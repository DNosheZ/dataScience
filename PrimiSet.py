for _ in range(int(input())):
  LstRq=[int(x) for x in input().split()]
  N, P=LstRq[0], LstRq[1]
  LstPrv=[int(y) for y in input().split()]

#si en LstPrv estan todos los divisores de P
print('Es Primiconjunto')
#caso contrario
print('No es Primiconjunto')
  
