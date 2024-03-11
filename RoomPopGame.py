Room=[]
while True:
    k=int(input())
    Incr=k+1
    Dcr=k-1
    if k==0:
        if len(Room)==0:print(0)
        else:print(' '.join(str(n) for n in Room))
        break
    elif k in Room:Room.pop(Room.index(k))
    else:#what if both Incr and Dcr are in the Room
        #I should erease both or just one, and wich and I have to pop()?
        if Incr in Room: Room.pop(Room.index(Incr))
        elif Dcr in Room: Room.pop(Room.index(Dcr))
        else: Room.append(k)
