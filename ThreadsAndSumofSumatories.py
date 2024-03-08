from threading import Thread
from threading import get_ident
from time import sleep

def sumatoria (inf,sup):
     global suma
     for i in range (inf, sup+1):
          suma+=i
     return suma
suma=0
hilo1 = Thread(target=sumatoria, args=(45, 72))
hilo2 = Thread(target=sumatoria, args=(73, 95))
hilo1.start()
hilo2.start()
print(f'{hilo1+hilo2}')
hilo1.join()
hilo2.join()
sleep(1)
