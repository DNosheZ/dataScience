for i in range(int(input())):
  N=int(input())
  NList=tuple(map(int,input().split()))
  Index=0
  for j in range(1,N+1):
    if j==1:
      SQR=NList[j-1]
    else:
      SQR=NList.index(SQR)+SQR
    if SQR==NList[0]:
      print(SQR)
      break
    elif j==N:
      print(SQR)
    elif SQR>len(NList):
      print(NList[N])
    elif SQR:
      print(NList[0])
    #falta el criterio de indice fuera de rango menor 
      
      
  
    
 

3
5
1 1 1 1 1
4
3 -1 4 -2
6
4 -3 5 -2 -1 6

5
3
4
