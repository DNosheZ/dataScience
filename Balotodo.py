Ballots = {}
M = int(input())

while True:
    Entrada = input().split(' ')
    
    if Entrada[0] == 'end':
        G = sum(1 for x in Ballots.values() if x[1] == 1)
        if G==0: print(0)
        break
    elif Entrada[0] == 'sms':
        if Entrada[1] not in Ballots:
            Ballots[Entrada[1]] = [1, 0]
        else:
            Ballots[Entrada[1]][0] += 1
            
            if Ballots[Entrada[1]][1] == 1:
                G = sum(1 for x in Ballots.values() if x[1] == 1)
                print(f"{Entrada[1]} {M // (Ballots[Entrada[1]][0] * G)}")

    elif Entrada[0] == 'winner':
        if Entrada[1] not in Ballots:
            Ballots[Entrada[1]] = [0, 1]
        else:
            Ballots[Entrada[1]][1] = 1
