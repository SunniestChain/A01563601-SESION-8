print (' 0 para salir')
numero = 1
promedio = 0
count = 0
suma = 0
while numero > 0 and numero !=0:
    numero = float(input('calificacion: '))
    suma += numero
    count +=1
    promedio = suma/count
    print('promedio actual: ',promedio)
    

print('salio')