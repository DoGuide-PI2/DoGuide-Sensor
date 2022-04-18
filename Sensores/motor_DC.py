 #biblioteca 
 class DCMotor:      
  def __init__(self, pin1, pin2,pin3,pin4,pin5, pin6,pin7,pin8, enable_pin1,enable_pin2,enable_pin3,enable_pin4, min_duty=750, max_duty=1023): # definição das portas
        self.pin1=pin1 #polo negativo do motor dianteiro esquerdo
        self.pin2=pin2 #polo positivo do motor dianteito esquerdo
        self.pin3=pin3 #polo negativo do motor dianteiro direito
        self.pin4=pin4 #polo positivo do motor dianteiro direito
        self.pin5=pin5 #polo negativo do motor traseiro esquerdo
        self.pin6=pin6 #polo positivo do motor traseiro esquerdo
        self.pin7=pin7 #polo negativo do motor traseiro direito
        self.pin8=pin8 #polo positivo do motor traseiro direito
        self.enable_pin1=enable_pin1 #pwm do motor dianteiro esquerdo
        self.enable_pin2=enable_pin2 #pwm do motor dianteiro direito
        self.enable_pin3=enable_pin3 #pwm do motor traseiro esquerdo
        self.enable_pin4=enable_pin4 #pwm do motor traseiro direito
        self.min_duty = min_duty # ciclo util minimo
        self.max_duty = max_duty # ciclo util maximo

  def forward(self,speed): # para frente
    self.speed = speed # polos positivos recebem '1' e os negativos recebem '0'
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)
    self.pin3.value(0)
    self.pin4.value(1)

    self.pin5.value(0)
    self.pin6.value(1)
    self.pin7.value(0)
    self.pin8.value(1)
    
  def backwards(self, speed):# para tras
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(1) # polos positivos recebem '0' e os negativos recebem '1'
    self.pin2.value(0)
    self.pin3.value(1)
    self.pin4.value(0)

    self.pin5.value(1)
    self.pin6.value(0)
    self.pin7.value(1)
    self.pin8.value(0)

  def stop(self): #parar
    self.enable_pin.duty(0)
    self.pin1.value(0) #todos os polos recebem '0'
    self.pin2.value(0)
    self.pin3.value(0)
    self.pin4.value(0)

    self.pin5.value(0)
    self.pin6.value(0)
    self.pin7.value(0)
    self.pin8.value(0)
  
  def left(self,speed): # para esquerda
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0) # polos positivos dos motores da direita recebem '1' e os outros recebem '0'
        self.pin2.value(0)
        self.pin3.value(0)
        self.pin4.value(1)

        self.pin5.value(0)
        self.pin6.value(0)
        self.pin7.value(0)
        self.pin8.value(1)

  def right(self,speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0) # polos positivos dos motores da esquerda recebem '1' e os outros recebem '0'
        self.pin2.value(1)
        self.pin3.value(0)
        self.pin4.value(0)

        self.pin5.value(0)
        self.pin6.value(1)
        self.pin7.value(0)
        self.pin8.value(0)
    
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle
   

    #codigo dos motores

from machine import Pin, PWM   
from time import sleep     
frequency = 15000       
pin1 = Pin(14, Pin.OUT)    
pin2 = Pin(27, Pin.OUT)
pin3 = Pin(17, Pin.OUT)    
pin4 = Pin(4, Pin.OUT)
pin5 = Pin(16, Pin.OUT)    
pin6 = Pin(12, Pin.OUT)
pin7 = Pin(4, Pin.OUT)    
pin8 = Pin(15, Pin.OUT)     
enable_pin1 = PWM(Pin(13), frequency)  
enable_pin2 = PWM(Pin(13), frequency) 
enable_pin3 = PWM(Pin(13), frequency)  
enable_pin4 = PWM(Pin(13), frequency)     
dc_motor = DCMotor(pin1, pin2,pin3,pin4,pin5, pin6,pin7,pin8, enable_pin1,enable_pin2,enable_pin3,enable_pin4, 350, 1023)
