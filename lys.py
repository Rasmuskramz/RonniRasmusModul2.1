# from random import random
from gpiozero import LED
from time import sleep
# Lys 1
led1=LED(16) # Gron
led2=LED(20) # Gul
led3=LED(21) # Rod
# Lys2
led4=LED(17) # Gron
led5=LED(27) # Gul
led6=LED(22) # Rod


def state0():
  #  print('Gron Kor!')
    led1.on()
    led6.on()
    sleep(3.5)
    led1.off()
    led6.off()
    return state1()

def state1():
  #  print('Gul stop')
    led2.on()
    led5.on()
    sleep(0.3)
    led6.on()
    sleep(1.5)
    led2.off()
    led5.off()
    led6.off()

    return state2()

def state2():
  #  print('Rod stop')
    led3.on()
    led4.on()
    sleep(5.5)
    led3.off()
    led4.off()
    return state3()

def state3():
  #  print('Gor')
  #  print('Klar!')
    led5.on()
    led3.on()
    sleep(0.3)
    led2.on()
    sleep(5.5)
    led5.off()
    led3.off()
    led2.off()
    return state0()
state=state0
while state: state=state()
print('Done')

