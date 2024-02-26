N=int(input())
LstNums=sorted(tuple(map(int, input().split())))
M=int(input())
LstRq=tuple(map(int, input().split()))
Sum=0
for i in range(M):
  QNum=LstRq[i]
  if QNum in LstNums:
    Sum+=LstNums.index(QNum)+1
  else:
    Sum+=0
print(Sum)

6
12 25 36 47 53 71
3
47 24 12


5
