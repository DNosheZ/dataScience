N=int(input())
Dic={}
for _ in range(N):
    Expression=input().split(' ')
    if Expression[0] not in Dic:Dic[Expression[0]]=Expression[1]

for _ in range(N):
    ToTraduce=input()
    if ToTraduce=='#':continue
    if ToTraduce in Dic:print(Dic[ToTraduce])
    else:print('Entrada no encontrada')