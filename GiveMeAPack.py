#Insert n, and get n-promotions with xE [2,5] platforms

#Dictonary with platforms 

plats1 = {
1: ("Disney+", 2900, 7000),
2: ("Prime Video", 4000, 7000),
3: ("Netflix", 7900, 13000),
4: ("HboMAX", 2900, 7000),
5: ("Crunchyroll", None, None),  # Assuming you want to use None for missing values
6: ("Star+", None, None)
}
Recos=()

#input quantity of combos

for i in range(0,input()): 
    comboN=()

     #random quantity of platforms

    for j in range(0,random.randint(2,5)): comboN.append(plats1[random.randint(1,6))
    Recos.append(comboN)

c=1

for ComboReco in Recos:

    print(”Combo #”,c)

    c+=1

    TotalDistri=0

    TotalVenta=0
    for r in ComboReco: 

        print(f’{r[0]}-${r[1]}→${r[2]}’)

        TotalDistri+=r[1]

        TotalVenta+=r[2]

     print(f’Precio al distribuidor: ${TotalDistri}\n Precio al publico: ${TotalVenta}\n’)