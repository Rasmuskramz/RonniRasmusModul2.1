a = -10
b = 10
c = 11
d = 20
e = 21
f = 30
g = 31
number = input('Indstast nummer ')
print('Er nummeret mellem -10 og 10? ')
if int((a) <= int(number) <= int(b)):
    print('Ja det er det')
if (int(number) > int(b)):
    print('Nej det er det ikke')
#print(int(a) <= int(number) <= int(b))
print('Er nummeret mellem 11 og 20? ')
if int((c) <= int(number) <= int(d)):
    print('Ja det er det')
if (int(number) > int(d)):
    print('Nej det er det ikke')
#print((int(c) <= int(number) <= int(d)))
print('Er nummeret mellem 21 og 30? ')
if int((e) <= int(number) <= int(f)):
    print('Ja det er det')
if (int(number) > int(f)):
    print('Nej det er det ikke')
#print(int(e) <= int(number) <= int(f))
print('Er nummeret større end 31? ')
if (int(number) >= int(g)):
    print('Ja det er det')
if (int(number) < int(g)):
    print('Nej det er det ikke')
