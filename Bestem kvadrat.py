#Lavet af Ronni Sole
loop = 1

while loop==1:
    P=float(input('Indtast effekten på genstanden '))
    U=230
    I=P/U
    Q=I/1.12
    print('%4.2f'% Q, 'A')
    if  Q <= 10:
        print('Du skal bruge et 1,5 kvadrat kabel til din istallation')
    elif 10 <= Q <= 16:
        print('Du skal bruge et 2,5 kvadrat kabel til din installation')
    else:
        print('Den indtastede værdi stemmer ikke overens med kabelstørrelserne')
    fort = input('Vil du lave en ny beregning? (Ja/Nej) ')
    if 'ja'.startswith(fort.lower()):
            print('Vi fortsætter')
    else:
        print ("Ok, programmet afsluttes nu")
        loop = 0
#        break

