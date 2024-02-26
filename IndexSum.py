import bisect
N = int(input())
LstNums = [int(x) for x in input().split()] 
M = int(input())
LstRq = [int(x) for x in input().split()]
Sum = 0
for item in LstRq:
    index = bisect.bisect_left(LstNums, item)
    if index < N and LstNums[index] == item:  # Verifica que el item se encontró
        Sum += index + 1
print(Sum)
