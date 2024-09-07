Diccionario={}
while True:
    Entrada=input()
    if Entrada=='#':
        for ID, expresion in Diccionario.items():
            for j in range(1,len(expresion[0])):
                if expresion[0][0:j] in Diccionario and expresion[0][0:j]!=expresion[0] and expresion[0][j:] in Diccionario and expresion[0][j:]!=expresion[0]:
                    print(f'{Diccionario[expresion[0]][0]} = {Diccionario[expresion[0][0:j]][0]} + {Diccionario[expresion[0][j:]][0]}')
                    break
        break
    elif Entrada not in Diccionario:Diccionario[Entrada]=[Entrada,None,None,0]