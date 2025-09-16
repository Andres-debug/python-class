n = int(input("Ingrese un numero para calcular el factorial: "))

factorial = 1

while n>1:
    factorial *= n
    n -= 1

print(f"El factorial es: {factorial}")