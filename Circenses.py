for i in range(int(input())):
  M, N = tuple(map(int, input().split()))
  Money=tuple(map(int, input().split()))
  MoneyBack=[None]*M
  print(max(MoneyBack)-min(MoneyBack))
