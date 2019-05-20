def addition(x, y):
   return x + y

# Denne funktion operere med subtraktion
def subtraktion(x, y):
   return x - y

# Denne funktion operere med multiplikation
def multiplikation(x, y):
   return x * y

# Denne funktion operere med division
def division(x, y):
   return x / y

def prmenu():
    print("Hvilken regneform ønsker du at benytte? ")
    print("1.Addition")
    print("2.Subtraktion")
    print("3.Multiplikation")
    print("4.Division")
    print("5.Stop program")

prmenu()
valg = int(input("Vælg regneform, bekræft med Enter: "))
wh=1

while wh==1:
    if valg == 1:
        loop = 1

        while loop == 1:
            print('Du har valgt addition')
            num1 = int(input("Indtast første nummer : "))
            num2 = int(input("Indtast andet nummer: "))
            print(num1,"+",num2,"=", addition(num1,num2))
            fort = input('Vil du lave en ny beregning? (Ja/Nej) ')
            if 'ja'.startswith(fort.lower()):
                print('Vi fortsætter')
            else:
                print ("Ok, programmet afsluttes nu")
                loop = 0
                prmenu()
                valg=int(input("Vælg menu nr."))

    if valg == 2:
        loop = 1

        while loop == 1:
            print('Du har valgt subtrakion')
            num1 = int(input("Indtast første nummer : "))
            num2 = int(input("Indtast andet nummer: "))
            print(num1,"-",num2,"=", subtraktion(num1,num2))
            fort = input('Vil du lave en ny beregning? (Ja/Nej) ')
            if 'ja'.startswith(fort.lower()):
                print('Vi fortsætter')
            else:
                print ("Ok, programmet afsluttes nu")
                loop = 0
                prmenu()
                valg=int(input("Vælg menu nr."))

    if valg == 3:
        loop = 1

        while loop == 1:
            print('Du har valgt multiplikation')
            num1 = int(input("Indtast første nummer : "))
            num2 = int(input("Indtast andet nummer: "))
            print(num1,"*",num2,"=", multiplikation(num1,num2))
            fort = input('Vil du lave en ny beregning? (Ja/Nej) ')
            if 'ja'.startswith(fort.lower()):
                print('Vi fortsætter')
            else:
                print("Ok, programmet afsluttes nu")
                loop = 0
                prmenu()
                valg=int(input("Vælg menu nr."))

    if valg == 4:
        loop =1

        while loop == 1:
            print('Du har valgt division')
            num1 = int(input("Indtast første nummer : "))
            num2 = int(input("Indtast andet nummer: "))
            print(num1,"/",num2,"=", int(division(num1,num2)))
            fort = input('Vil du lave en ny beregning? (Ja/Nej) ')
            if 'ja'.startswith(fort.lower()):
                print('Vi fortsætter')
            else:
                print ("Ok, programmet afsluttes nu")
                loop = 0
                prmenu()
                valg=int(input("Vælg menu nr."))

    if valg == 5:
            print("Nu stopper programmet!!!")
            wh=2
