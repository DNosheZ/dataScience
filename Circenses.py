for i in range(int(input())):
  M, N = tuple(map(int, input().split()))
  Money=tuple(map(int, input().split()))
  MoneyBack=[None]*M
  i=0
  h=0
  while Money and h≤N:#verificando que haya dinero para repartir
    MoneyBack[i]+=Money[h]
    Money.remove(Money[h]) #eliminando los billetes ya tomados
    if i==(M-1):
        i=0
    else:
        i+=1
    h+=1
  print(max(MoneyBack)-min(MoneyBack))