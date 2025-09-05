frase = input('dame una frase matona: ')
contador_vocales = 0
indice = 0
while indice < len(frase):
    caracter = frase[indice].lower()
    print(caracter)
    indice += 1
    if caracter == 'a' or caracter =='e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contador_vocales += 1
print('El numero de vocales es: ',contador_vocales)

