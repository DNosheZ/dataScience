K=int(input())
Poles=[int(x) for x in input().split()]
for _ in range(int(input())):
  Poles2Quantify=[int(y) for y in input().split()]
  if all(Pole in Poles for Pole in Poles2Quantity):
    print(f"{max(Poles2Quantity)-min(Poles2Quantity)} kms")
