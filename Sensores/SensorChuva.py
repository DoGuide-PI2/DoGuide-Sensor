from machine import Pin
from time import sleep

d = Pin(32, Pin.IN) #Pino 32 como entrada

def loopreading():
    while True:
        if d.value() > 0:
            x = "No Rain"
        else:
            x = "Rain"
    sleep(1)
     
loopreading()