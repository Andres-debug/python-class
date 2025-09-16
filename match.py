print("Selecciona una operacion: ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Exponenciar")

opcion = int(input("Ingrese el numero de la operacion que quiere realizar: "))

# Solicitar los dos numeros para operar
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

match opcion:
    case 1:
        resultado = numero1 + numero2
        print(f"La suma es: {resultado}")
    case 2:
        resultado = numero1 - numero2
        print(f"La resta es: {resultado}")
    case 3:
        resultado = numero1 * numero2
        print(f"La multiplicacion es: {resultado}")
    case 4:
        if numero2 == 0:
            print("Error: No se puede dividir entre 0")
        else:
            resultado = numero1 / numero2
            print(f"La division es: {resultado}")
    case 5:
        resultado = numero1 ** numero2
        print(f"El resultado de la exponenciacion es: {resultado}")
    case _:
        print("Error: Opcion no valida. Por favor seleccione una opcion entre 1 y 5")
