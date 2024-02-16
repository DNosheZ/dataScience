N=int(input())
lstSo=tuple(map(int,input().split(', ')))
lstLar=tuple(map(int,input().split(', ')))
lstIs=tuple(map(int,input().split(', ')))
x=0 
y=0
z=0
for i in range(0,N):
  m= lstSo[i]+lstLar[i]+lstIs[i]
  if (lstSo[i]%2==0 and m%2==0) or (lstSo[i]%2!=0 and m%2!=0):
    x+=1
  if (lstLar[i]%2==0 and m%2==0) or (lstLar[i]%2!=0 and m%2!=0):
    y+=1
  if (lstIs[i]%2==0 and m%2==0) or (lstIs[i]%2!=0 and m%2!=0):
    z+=1
print(f'SO:{x}, LAR:{y}, IS:{z}')
