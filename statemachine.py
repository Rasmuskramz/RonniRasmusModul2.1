
from random import random
from time import sleep


def state0():
    print('\033[1;34;40m State0\n')

    sleep(1.5)
    if random() >= .5:
        return state1()
    else:
        return state2()

def state1():
    print('\033[1;30;47m State1\n')

    sleep(1.5)
    if random() >= .5:
        return state0()
    elif random() < .5:
        return state2()
    else:
        return state0()

def state2():
    print('\033[1;31;43m State2\n')

    sleep(.6)
    if random() < .5:
        return state0()
    else: exit('Færdig med states')


state = state0()

while state: state=state()

print('Færdig med states')
