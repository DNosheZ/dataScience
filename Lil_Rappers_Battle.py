import heapq
Alfa=[]
Beta=[]
Gamma=[]
heapq.heapify(Alfa)
heapq.heapify(Beta)
heapq.heapify(Gamma)
A_t_points=0
B_t_points=0
C_t_points=0
while True:
    A_player=None
    B_player=None
    C_player=None
    LstPart=[]
    cmd=input()
    if cmd=='fin del juego':
        print(f'Equipo A: {A_t_points}')
        print(f'Equipo B: {B_t_points}')
        print(f'Equipo C: {C_t_points}')
        break
    elif cmd=='menores':
        if len(Alfa)>=1:A_player=heapq.heappop(Alfa);LstPart.append(A_player)
        if len(Beta)>=1:B_player=heapq.heappop(Beta);LstPart.append(B_player)
        if len(Gamma)>=1:C_player=heapq.heappop(Gamma);LstPart.append(C_player)
        if len(LstPart)>=2:
            if A_player and A_player>=B_player and A_player>=C_player:A_t_points+=1
            elif B_player and B_player>=A_player and B_player>=C_player:B_t_points+=1
            elif C_player and C_player>=A_player and C_player>=B_player:C_t_points+=1
        continue
    else:
        Add=cmd.split()
        if Add[0]=='A': heapq.heappush(Alfa, int(Add[1]))
        elif Add[0]=='B': heapq.heappush(Beta, int(Add[1]))
        elif Add[0]=='C': heapq.heappush(Gamma, int(Add[1])) 
