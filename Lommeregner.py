# Denne funktion operere med addition
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

print("Hvilken regneform ønske du at benytte? ")
print("1.Addition")
print("2.Subtraktion")
print("3.Multiplikation")
print("4.Division")


valg = input("Vælg regneform, bekræft med Enter: ")

num1 = int(input("Indtast første nummer : "))
num2 = int(input("Indtast andet nummer: "))

if valg == '1':
   print(num1,"+",num2,"=", addition(num1,num2))

elif valg == '2':
   print(num1,"-",num2,"=", subtraktion(num1,num2))

elif valg == '3':
   print(num1,"*",num2,"=", multiplikation(num1,num2))

elif valg == '4':
   print(num1,"/",num2,"=", division(num1,num2))
else:
   print('Forkert indtastning, vælg venligst en korrekt menu.')
