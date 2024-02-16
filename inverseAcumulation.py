N=int(input())
lst=tuple(map(int,input().split()))
a=0
for i in range(0,N):
  a+=lst
  if i>=1:
    print(a)
  
  
  
