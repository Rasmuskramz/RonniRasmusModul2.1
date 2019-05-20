#Ronni
def spænding():
    print('Du har valgt spændingsberegneren')
    amp = int(input('Indtast strømmen'))
    modstand = int(input('Indtast modstanden'))
    value = int(amp*modstand)
    print('U=','%4.2f'% value, 'Volt')

def strøm():
    print('Du har valgt srømberegneren')
    volt = int(input('Indtast spændingen'))
    modstand = int(input('Indtast modstanden'))
    value = int(volt/modstand)
    print('I=','%4.2f'% value, 'A')

def modstand():
    print('Du har valgt modstandssberegneren')
    volt = int(input('Indtast spændingen'))
    amp = int(input('Indtast strømmen'))
    value = int(volt/amp)
    print('R=','%4.2f'% value, 'Ohm')

#Denne er lavet af Ronni Sole
def prmenu():
    print('Velkommen til min beregner jf. Ohm´s lov' )
    print('Bekræft dine valg med Enter')
    print("1) menu for spændingsberegning")
    print("2) menu for strømberegning")
    print("3) menu for modstandssberegning")
    print("4) stop program")

prmenu()
Menunr=int(input("Vælg menu nr."))
wh=1

while wh==1:
    if Menunr == 1:
        spænding()
        # Her skal det kode sættes ind som skal udføre et eller andet
        # print("du har valgt menu for strømberegning")
        # print('Dette er menuen for beregning af strøm jf. ohms lov')
        # volt = int(input('Hvilken spænding har du? '))
        # modstand = int(float(input('Hvilken modstand har du? ')))
        # = volt/modstand
        # print('%4.2f'% amp, 'Ampere')
        fort = input('Vil du lave en beregning mere? (Ja/Nej) ')
        if 'ja'.startswith(fort.lower()):
           print('Vi fortsætter')
        else:
           print("Ok, du får menupunkterne igen")
           prmenu()
           Menunr=int(input("Vælg menu nr."))

    if Menunr == 2:
        modstand()
        # Her skal det kode sættes ind som skal udføre et eller andet
        # print("du har valgt menu for modstandsberegning")
        # print('Dette er menuen for beregning af modstande jf. ohms lov')
        # volt = int(input('Hvilken spænding har du? '))
        # amp = int(float(input('Hvilken strøm har du? ')))
        # modstand = volt/amp
        # print('%4.2f'% modstand, 'Ohmsk modstand')
        fort1 = input('Vil du lave en beregning mere? (Ja/Nej)  ')
        if 'ja'.startswith(fort1.lower()):
            print('Vi fortsætter')
        else:
            print("Ok, du får menupunkterne igen")
            prmenu()
            Menunr = int(input("Vælg menu nr."))

    if Menunr == 3:
        # Her skal det kode sættes ind som skal udføre et eller andet
        strøm()
        # print("du har valgt menu for spændingsberegning")
        # print('Dette er menuen for beregning af strøm jf. ohms lov')
        # amp = int(float(input('Hvilken strøm har du? ')))
        # modstand = int(float(input('Hvilken modstand har du? ')))
        # volt = amp*modstand
        # print('%4.0f'% volt, 'Volt')
        fort2 = input('Vil du lave en beregning mere? (Ja/Nej) ')
        if 'ja'.startswith(fort2.lower()):
            print('Vi fortsætter')
        else:
            print ("Ok, du får menupunkterne igen")
            prmenu()
            Menunr = int(input("Vælg menu nr."))

    if Menunr == 4:
        print("Nu stopper programmet!!!")
        wh=2

