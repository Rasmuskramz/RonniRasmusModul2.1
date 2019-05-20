#Ronni Sole

a = 0
b = 10
c = 11
d = 20
e = 21
f = 30
g = 31
h = 40
number = int(input('Indstast nummer '))

# if int(number) >= 0 and int(number <= 40):
if int(a <= number <= h):
    print('Er nummeret mellem', a, 'og', b, '? ')
    if int(a <= number <= b):
        print('Ja det er det')
    elif int(number > b):
        print('Nej det er det ikke')
        print('Er nummeret mellem', c, 'og', d, '? ')
    if int(c <= number <= d):
        print('Ja det er det')
    elif int(number > d):
        print('Nej det er det ikke')
        # print((int(c) <= int(number) <= int(d)))
        print('Er nummeret mellem', e, 'og', f, '? ')
    if int(e <= number <= f):
        print('Ja det er det')
    elif int(number > f):
        print('Nej det er det ikke')
        # print(int(e) <= int(number) <= int(f))
        print('Er nummeret mellem', g, 'og', h, '? ')
    if int(g <= number <= h):
        print('Ja det er det')
    elif int(number > h):
        print('Nej det er det ikke')
else:
    print('Tallet er udenfor område')
