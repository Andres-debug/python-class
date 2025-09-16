import re

password = input("Ingrese su contraseña: ")

if len(password)<8:
    print("La contraseña debe tener por lo menos 8 caracteres")

elif not re.search(r'[A-Z]',password):
    print("La contraseña debe contener al menos una letra mayuscula.")
elif not re.search(r'[0-9]',password):
    print("La contraseña debe tener al menos un numero")
elif not re.search(r'[@#$%^&+=]',password):
    print("La contraseña debe tener al menos un caracter epecial")
else:
    print("La contraseña es segura")
