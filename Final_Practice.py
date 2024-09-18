Equipos=dict()
#Equipos={
#'atl':{
#         'año':[1/0,1/0,1/0],
#         'año2':[1/0,1/0,1/0],

# #     },
#   'env':{
#       'año1':[1/0,1/0,1/0],
#       'año2':[1/0,1/0,1/0],
#   }
# 
# 
# 
# 
#}
while True:
    Entrada=input().split()
    #[nombre,año,copa]
    if Entrada[0]=='#':
        for equipo, sub_diccionario in Equipos.items():
            R=[0,0,0]
            for año, value in sub_diccionario.items():
                R[0]+=Equipos[equipo][año][0]
                R[1]+=Equipos[equipo][año][1]
                R[2]+=Equipos[equipo][año][2]

            if R > [0, 0, 0]:
                # Imprimir clave y la suma de las primeras 3 características
                print(f'{equipo}, {sum(R)}')
        break
    elif Entrada[0] not in Equipos.keys():#primera vez que se registra el equipo como ganador

        if Entrada[2]=='nal':Equipos[Entrada[0]]={Entrada[1]:[1,0,0]}
        elif Entrada[2]=='lib':Equipos[Entrada[0]]={Entrada[1]:[0,1,0]}
        elif Entrada[2]=='sud':Equipos[Entrada[0]]={Entrada[1]:[0,0,1]}
    else:#el equipo ya ha ganado al menos una copa
        if Entrada[1] not in Equipos[Entrada[0]].keys() :#ese año aun no han ganado
            #se agrega ese año, y segun el equipo ganador se asigna [1,0,0], [0,1,0] o [0,0,1]
            if Entrada[2]=='nal':Equipos[Entrada[0]][Entrada[1]]=[1,0,0]
            elif Entrada[2]=='lib':Equipos[Entrada[0]][Entrada[1]]=[0,1,0]#equipo en año entrada[1] gano copa lib
            elif Entrada[2]=='sud':Equipos[Entrada[0]][Entrada[1]]=[0,0,1]
        else:#ese año ya ganaron
            if Entrada[2]=='nal' and Equipos[Entrada[0]][Entrada[1]][0]==0:#aun no ha ganado esa copa
                Equipos[Entrada[0]][Entrada[1]][0]=1
            elif Entrada[2]=='lib' and Equipos[Entrada[0]][Entrada[1]][1]==0:#aun no ha ganado esa copa
                Equipos[Entrada[0]][Entrada[1]][1]=1
            elif Entrada[2]=='sud' and Equipos[Entrada[0]][Entrada[1]][2]==0:#aun no ha ganado esa copa
                Equipos[Entrada[0]][Entrada[1]][2]=1
        
