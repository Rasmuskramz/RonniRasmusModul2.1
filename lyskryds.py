from time import sleep


def state0():
    print('\033[1;32;32m Kør!\n')
    sleep(.5)
    return state1()

def state1():
    print('\033[1;33;33m Væk!\n')
    sleep(.5)
    return state2()


def state2():
    print('\033[1;31;31m Stop!\n')
    sleep(.5)
    return state3()

def state3():
    print('\033[1;31;31m Gør')
    print('\033[1;33;33m Klar!')
    sleep(2.5)
    return state0()

state = state2()

while state: state=state()

