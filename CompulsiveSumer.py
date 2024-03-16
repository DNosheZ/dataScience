import heapq
C=int(input())
for _ in range(C):
  Set=list(map(int,input().split))
  if Set[-1]!=-1:continue
  Set.pop()
  while True:
    InstantSum=0
    if len(Set)==2:break
    for _ in range(2):
      M=heapq.heappop()
      InstantSum+=M
    heapq.heappush(Set,InstantSum)
  print(' '.join(list(map(str,Set))))

