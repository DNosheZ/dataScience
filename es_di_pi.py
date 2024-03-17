import heapq
Track=0
Inits=[]
Divs=[]
heapq.heapify(Inits)
Duracion=int(input())
N=int(input())
for _ in range(N):
    Tone=list(map(int,input().split()))#[#_of_tone, start_tone_msg, each_msg_pinch_this_tone]
    heapq.heappush(Inits,Tone.pop(1))
    Divs.append(Tone[1])
while True:
    if Track==Duracion:break
    divi=sum(1 for div in Divs if Track%div==0)
    if Track==Inits[0] or divi>=1: 
        for _ in range(divi): print(Track)
        if Track==Inits[0]:heapq.heappop(Inits)
