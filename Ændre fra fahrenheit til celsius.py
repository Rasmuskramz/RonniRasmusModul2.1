# TODO: type solution here
def conversion(fahrenheit):
        celsius = (fahrenheit - 32) * (5/9)
        return celsius

input = float(input('Hvad er temperaturen i Fahrenhiet? '))

print("Temperaturen i Celsius er:  " + str(conversion(input)) + " grader.")
