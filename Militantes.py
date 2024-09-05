Votations={}
while True:
    Entrada=input().split(' ')
    if Entrada[0]=="#":
        solo_uno=0
        dos_unos=0
        tres_unos=0
        for ID, votos in Votations.items():
            count_ones = sum(votos)  # Contamos la cantidad de '1's en cada registro
            if count_ones == 1:
                solo_uno+=1
            elif count_ones == 2:
                dos_unos+=1
            elif count_ones == 3:
                tres_unos+=1
        print(f'{solo_uno} {dos_unos} {tres_unos}')
        break


    elif int(Entrada[0]) not in Votations and Entrada[1]=='pdd':Votations[int(Entrada[0])]=[1,0,0]    
    elif int(Entrada[0]) not in Votations and Entrada[1]=='pdi':Votations[int(Entrada[0])]=[0,1,0]
    elif int(Entrada[0]) not in Votations and Entrada[1]=='pdc':Votations[int(Entrada[0])]=[0,0,1]
    elif int(Entrada[0]) in Votations and Entrada[1]=='pdd':Votations[int(Entrada[0])][0]=1
    elif int(Entrada[0]) in Votations and Entrada[1]=='pdi':Votations[int(Entrada[0])][1]=1
    elif int(Entrada[0]) in Votations and Entrada[1]=='pdc':Votations[int(Entrada[0])][2]=1