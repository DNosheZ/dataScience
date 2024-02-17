N=int(input())
lst=tuple(map(str,input().split(', ')))
h=0
w=''
for i in range(0,N):
  if i==0 or i%2==0:
    w+=lst[int(i/2)]
  elif i%2!=0:
    h+=1
    w+=lst[N-h]
print(w)
