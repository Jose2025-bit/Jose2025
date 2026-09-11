import string
import random

longitud = int(input("ingresa el tama;o de la contrase;a: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

print(caracteres)

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print ("La contrase;a es: " + contrasena)

