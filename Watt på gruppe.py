# Ronni Sole

tæller = 1
total = 0
u = 230

print('Efter indtastning bekræft med Enter!')
while tæller:
    tæller += 1
    total += int(input("Hvor mange watt er apparatet på? : "))
    fort = input('Vil du indtaste en enhed mere? ')
    if 'ja'.startswith(fort.lower()):
        print('Vi fortsætter')
    else:
        print ("Ok, her er din optælling")
        break
print('Samlede belastning af gruppen', total,'watt')
print(tæller - 1, 'enheder')
print(total/u, 'Ampere')
