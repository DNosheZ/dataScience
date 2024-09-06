Libros={}
Fernando=0
Gustavo=0
while True:
    Entrada=input().split(' ')
    if Entrada[0]=='0':
        for ID, libro in Libros.items():
            if 'F' in libro and 'G' in libro and ID%2==0:Fernando+=1
            elif 'F' in libro and 'G' in libro and ID%2!=0:Gustavo+=1
            if 'F' in libro and 'G' not in libro:Fernando+=1
            elif 'F' not in libro and 'G' in libro:Gustavo+=1
            
        print(f'{Fernando} {Gustavo}')
        break
    elif Entrada[1]=='F' and int(Entrada[0]) not in Libros:Libros[int(Entrada[0])]=['F',None]
    elif Entrada[1]=='G' and int(Entrada[0]) not in Libros:Libros[int(Entrada[0])]=[None,'G']
    elif Entrada[1]=='F' and int(Entrada[0])  in Libros:Libros[int(Entrada[0])][0]='F'
    elif Entrada[1]=='G' and int(Entrada[0])  in Libros:Libros[int(Entrada[0])][1]='G'
    