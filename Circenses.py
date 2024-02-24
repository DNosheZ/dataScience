for i in range(int(input())):
  M, N = tuple(map(int, input().split()))
  Money=tuple(map(int, input().split()))
  MoneyBack=[0]*M
  i=0
  for h in range(N):
    MoneyBack[i]+=Money[0]
    Money=Money[1:]
    if i==(M-1):
        i=0
    else:
        i+=1
  print(max(MoneyBack)-min(MoneyBack))
