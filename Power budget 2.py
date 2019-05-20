#Denne er lavet af Rasmus Kramer & Ronni Sole
import math

def prmenu():
    print('Velkommen til vores fiber power budget beregner' )
    print('Bekræft dine valg med Enter')
    print("Tast 1 hvis dit kabel er længere end 2KM")
    print("Tast 2 hvis dit kabel er kortere end 2KM")
    print("Tast 3 for at stoppe programmet")

def valg():
    print('Velkommen til vores fiber power budget beregner' )
    print('Bekræft dine valg med Enter')
    print("Tast 1 hvis du vil benytte singlemode kabel")
    print("Tast 2 hvis du vil benytte multimode kabel")
    print("Tast 3 for at stoppe programmet")

prmenu()
Menunr=int(input("Vælg menu nr."))
wh=1

a = 0
b = -3


while wh==1:
    if Menunr == 1:
        print("Beregning af singlemode kabel")
        print('Bekræft alle indtastninger med Enter')
        # Længde på kabel
        lang = int(float(input('Hvor langt er dit kabel angivet i KM? ')))
        lang2 = (lang*0.35)
        print(lang2)
        # Antal splidsninger og dæmpning deraf
        splid = int(float(input('Hvor mange splidsninger har du? ')))
        splid2 = (splid*0.1)
        print(splid2)
        # Antal konnektorer og dæmpning deraf
        konn = int(float(input('Hvor mange konnektorer har du? ')))
        konnektor = (konn*0.5)
        print(konnektor)
        # Udstyrsdæmpning
        trans = int(float(input('Hvor mange dBm sender din transmitter ud? ')))
        reciever = int(float(input('Hvor stor følsomhed har din reciever? ')))
        # Sikkerhedsmargin
        sikkerhed = 3
        # Fremtidig reperation
        if lang<10:
            L=1
        else:
            L=lang
        frem = (math.ceil(L/10)*0.5)
        print(frem)
        # Beregning
        damp = ((trans-reciever)+(frem+sikkerhed+konnektor+splid2+lang2))
        print(trans, '-', reciever)
        print(frem,'+', sikkerhed, '+', konnektor, splid2, '+', lang2)

        if (damp > a):
            print('Du har', damp,'DB dæmpning')
            print("OK")
        elif (damp >= b):
            print('Fint')
            print('Du har', damp,'DB dæmpning')
        else:
            print('Du har', damp,'DB dæmpning')
            print('Dur ikke - om igen!')
        # print('%4.2f'% damp, 'DB')
        prmenu()
        Menunr=int(input("Vælg menu nr."))
        '''
        fort = input('Vil du lave en beregning mere? (Ja/Nej) ')
        
        if 'ja'.startswith(fort.lower()):
            print('Vi fortsætter')
           # valgnr = 1
        else:
            print("Ok, du får menupunkterne igen")
            prmenu()
            Menunr=int(input("Vælg menu nr."))
        '''

    if Menunr == 2:
        valg()
        valgnr=int(input("Vælg menu nr."))
    if Menunr == 3:
        print("Nu stopper programmet!!!")
        wh=2

    if Menunr == 4:
        print("Beregning af multimode kabel")
        print('Bekræft alle indtastninger med Enter')
        # Længde på kabel
        lang = int(float(input('Hvor langt er dit kabel angivet i KM? ')))
        lang2 = (lang*0.35)
        # Antal splidsninger og dæmpning deraf
        splid = int(float(input('Hvor mange splidsninger har du? ')))
        splid2 = (splid*0.1)
        # Antal konnektorer og dæmpning deraf
        konn = int(float(input('Hvor mange konnektorer har du? ')))
        konnektor = (konn*0.5)
        # Udstyrsdæmpning
        trans = int(float(input('Hvor mange dBm sender din transmitter ud? ')))
        reciever = int(float(input('Hvor stor følsomhed har din reciever? ')))
        # Sikkerhedsmargin
        sikkerhed = 3
        # Fremtidig reperation
        if lang<10:
            L=1
        else:
            L=lang
        frem = (math.ceil(L/10)*0.5)
        print(frem)
        # Beregning
        damp = ((trans-reciever)-(frem+sikkerhed+konnektor+splid2+lang2))
        if (damp > a):
            print('Du har', damp,'DB dæmpning')
            print("OK")
        elif (damp >= b):
            print('Fint')
            print('Du har', damp,'DB dæmpning')
        else:
            print('Du har', damp,'DB dæmpning')
            print('Dur ikke - om igen!')
        # print('%4.2f'% damp, 'DB')
        prmenu()
        Menunr=int(input("Vælg menu nr."))
        '''
        fort = input('Vil du lave en beregning mere? (Ja/Nej) ')
        
        if 'ja'.startswith(fort.lower()):
            print('Vi fortsætter')
        else:
            print("Ok, du får menupunkterne igen")
            prmenu()
            Menunr=int(input("Vælg menu nr."))
        '''

    if valgnr == 1:
        Menunr = 1
    if valgnr == 2:
        Menunr = 4


