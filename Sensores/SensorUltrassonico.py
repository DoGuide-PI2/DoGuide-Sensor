# Importação das bibliotecas
from Sensores.hcsr04 import HCSR04 
from time import sleep
 
# ESP32
sensor_frontal_1 = HCSR04(trigger_pin=19, echo_pin=18, echo_timeout_us=10000)
sensor_frontal_2 = HCSR04(trigger_pin=25, echo_pin=33, echo_timeout_us=10000)
sensor_buracos = HCSR04(trigger_pin=34, echo_pin=35, echo_timeout_us=10000)
sensor_altura = HCSR04(trigger_pin=39, echo_pin=36, echo_timeout_us=10000)
 
while True:
    distance1 = sensor_frontal_1.distance_cm()  #Todas as distancias em cm
    distance2 = sensor_frontal_2.distance_cm()
    distance3 = sensor_buracos.distance_cm()
    distance4 = sensor_altura.distance_cm()
 
    if (distance1 <= 200) | (distance2 <= 200): #Se detectado objeto 2 metros (200cm) a frente ou menos que isso
        print("Objeto a frente")
    elif (distance3 > 17.407): #A distancia do HCSR04 até o chão é esse valor, se a distancia for maior que isso até a deteccao de um objeto, isso eh um buraco. 
        print("Buraco")
    elif (distance4 <= 200):
        print("Objeto acima")

    sleep(1) # A distância será atualizada a cada 1 segundo