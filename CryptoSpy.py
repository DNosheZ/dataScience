for i in range(0,int(input())):
  lstPal=tuple(map(str,input().split()))
  NewlstPal=[]
  leN=len(lstPal)
  for j in range(0,leN//2):
    NewlstPal+=lstPal[leN-2-2*j:leN-2*j]
  if leN%2!=0:
      print(''.join(NewlstPal+[lstPal[0]]))
  else:
      print(''.join(NewlstPal))
