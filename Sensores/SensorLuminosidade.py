from machine import Pin, ADC
from time import sleep

ldr= ADC(Pin(23)) 
relay = Pin(1, Pin.OUT)

ldr.atten(ADC.ATTN_11DB)  #conversão de 0 a 4095

ldr_value = ldr.read( ) #salva o valor

def loopreading():
    while True: 
        if (ldr_value >= 0 and ldr_value <= 1000):  #O valor de 1000 foi usado para o limite de incidência de luz
            relay.value(0) #Este relé é acionado no nível baixo
        return 'z'
        else:
            relay.value(1)
        sleep(3) 

loopreading()
