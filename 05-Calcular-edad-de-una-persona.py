#Calcular edad de una persona

print("******************************")
print("*Calcular edad de una persona*")
print("****************************** \n")

from datetime import datetime

now = datetime.now()
year = format (now.year)
year = int(year)
print(year)
yearbirth = int(input("¿Cual es tu año de nacimiento? \n"));

edad = year - yearbirth;

print("Tu edad es: ", edad, ", ya estas viejo :)");
