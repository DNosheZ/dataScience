#Insert n, and get n-promotions with xE [2,5] platforms
import random
#Dictonary with platforms 

plats1 = {
1: ("Disney+", 2900, 7000), #(Platform name, providers price, distribiton price)
2: ("Prime Video", 4000, 7000),
3: ("Netflix", 7900, 13000),
4: ("HboMAX", 2900, 7000),
5: ("Crunchyroll", 6000, 9000),  # Assuming you want to use None for missing values
6: ("Star+", 5000, 9000)
}
Recos=[]
#list of recomended combos

#input quantity of combos

for i in range(0,int(input("Ingrese el numero de combos a generar: "))): 
    comboN=[]#list with the platforms in the combo

     #random quantity of platforms
    numPlatChoice=input("Quiere su combo con un numero preciso de plataformas(P), o una cantidad aleatorio)(A)? (P/A): ").upper()
    while (numPlatChoice!=("P" or "A")):
        print("Error al elegir; recuerde que las opciones son P o A")
        numPlatChoice=input("Quiere su combo con un numero preciso de plataformas(P), o una cantidad aleatorio)(A)? (P/A): ").upper()
    if numPlatChoice==("P"): numPlat=int(input("Ingrese la cantidad de plataformas para este combo: "))
    elif numPlatChoice==("A"): numPlat=random.randint(2,5)
    for j in range(0,numPlat):
        platToCombo=plats1[random.randint(1,6)]
        if (platToCombo) not in comboN:
            pass
        else:
            platToCombo=plats1[random.randint(1,6)]
        comboN.append(platToCombo)

        
    Recos.append(comboN)

c=1#combo counters
for ComboReco in Recos:

    print(f'Combo # {c}')

    c+=1

    TotalDistri=0

    TotalSell=0
    for r in ComboReco: 

        print(f'{r[0]}: ${r[1]} → ${r[2]}')

        TotalDistri+=r[1]

        TotalSell+=r[2]

    print(f'Precio al distribuidor: ${TotalDistri}\nPrecio al publico: ${TotalSell}\n')
#next update: we cant have two combos with similar platforms included
