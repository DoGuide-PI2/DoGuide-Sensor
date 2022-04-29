from machine import Pin
from time import sleep

d = Pin(32, Pin.IN) #Pino 32 como entrada

def loopreading():
    while True:
        if d.value() > 0: #A detecção de chuva funcionará quando for detectado nível baixo
            x = "No Rain"
        else:
            x = "Rain"
            return 'r'   #A string de retorno para o caso da identificação de chuva. Se não for detectado, retornará ao loop de leitura.
    sleep(1)
     
loopreading()
