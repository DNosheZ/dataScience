M=int(input())
LstM=[]
while True:
    Num=int(input())
    if Num==0:break
    LstM.append(Num)
    LstM.append(Num)
    if len(LstM)%5==0:
        Yayo=sorted(LstM)
        if len(Yayo)%2==0:
            Bam=(Yayo[len(Yayo)/2 -1]+Yayo[len(Yayo)])
            if Bam%2!=0:
                print(f'{Bam}/2')
            else:print(int(Bam/2))
        else:
            Kaos=Yayo[int(len(Yayo)+0.5)]
            print(Kaos)
