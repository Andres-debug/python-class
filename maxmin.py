numeros = [12,5,8,13,2,45,7,1,78]

maximo = numeros[0]
minimo = numeros[0]

for num in numeros:
    if num > maximo:
        maximo = num
    elif num < minimo:
        minimo = num

print(maximo)
print(minimo)