#Lista de notas
notas = [9,10,7,5,1,11,8]

#Variables para el calculo del promedio

total_notas = 0
cantidad_notas = 0

#Validar y calcualr el promedio

for nota in notas:
    if 0 <= nota <= 10:
        total_notas += nota
        cantidad_notas +=1
    else:
        print(f"La nota {nota} no es valida")

if cantidad_notas > 0:
    promedio = total_notas/cantidad_notas
    print(f"El promedio de las notas validas es: {promedio}")
    print(f"Cantidad de notas validas {cantidad_notas}")
else:
    print("No hay notas validas para calcular el promedio")
