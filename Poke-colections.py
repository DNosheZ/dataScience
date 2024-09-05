Valen={}
Felipe={}
while True:
    Entrada=input().split(' ')
    if Entrada[0]=='#':
        dif=set(Valen.keys) ^ set(Felipe.keys)
        print(f'{len(Valen)} {len(Felipe)} {len(dif)}')
        break
    elif Entrada[0]=='V' and int(Entrada[1]) not in Valen:Valen[int(Entrada[1])]=None
    elif Entrada[0]=='F' and int(Entrada[1]) not in Felipe:Felipe[int(Entrada[1])]=None

Valen = {}
Felipe = {}

while True:
    Entrada = input().split(' ')
    if Entrada[0] == '#':
        # Convertir las claves de los diccionarios en conjuntos para hacer la diferencia simétrica
        diferencia_simetrica = set(Valen.keys()) ^ set(Felipe.keys())
        print(f'{len(Valen)} {len(Felipe)} {len(diferencia_simetrica)}')
        break
    elif Entrada[0] == 'V' and int(Entrada[1]) not in Valen:
        Valen[int(Entrada[1])] = None
    elif Entrada[0] == 'F' and int(Entrada[1]) not in Felipe:
        Felipe[int(Entrada[1])] = None
