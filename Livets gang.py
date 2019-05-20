import time

y=0
tid=1

def home(x):
    global y
    global tid
    y=y+1
    print('Y='+str(y))
    if y==5:
        return

    if x=='wake':
        x='train'
        print('take train work')
        time.sleep(tid)
        return work(x)
    elif x=='train':
        x='sleep'
        print('Går i seng')
        time.sleep(tid)
        return bed(x)

def work(x):
    if x=='train':
        x='train'
        print('take train home')
        time.sleep(tid)

        return home(x)


def bed(x):
    if x=='sleep':
        x='wake'
        print('Vågner')
        time.sleep(tid)
        return home(x)

state=home(x='wake')
while state: state=home(x='wake')
print('Død og færdig')
