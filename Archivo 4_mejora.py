
'''
Reto 1
Entradas: monto(int)
Salidas: desglosarBilletes(str)
Restricciones: monto(Debe ser un número entero positivo) 
'''
def desglosarBilletes(monto):
    if monto % 1000 != 0:
        return -1

    denominaciones = [20000, 10000, 5000, 2000, 1000]
    resultado = []

    for denominacion in denominaciones:
        cantidad = monto // denominacion
        resultado.append([cantidad, denominacion])
        monto -= cantidad * denominacion

    return resultado

#print(desglosarBilletes(125000))


'''
Reto 2
Entradas: 
mensaje(str)
caracter(str)
indice(str)
Salidas: cifradoCesar(str)
Restricciones: mensaje(Debe ser una cadena de caracteres)
'''
def cifradoCesar(mensaje):
    if not isinstance(mensaje, str) or len(mensaje) == 0:
        return ""

    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje_cifrado = ""

    for caracter in mensaje:
        if caracter == " ":
            mensaje_cifrado += " "
        else:
            caracter_mayus = caracter.upper()
            if caracter_mayus in abecedario:
                indice = abecedario.index(caracter_mayus)
                caracter_cifrado = abecedario[(indice + 3) % 26]
                mensaje_cifrado += caracter_cifrado
            else:
                mensaje_cifrado += caracter

    return mensaje_cifrado
#print(cifradoCesar("Hoy es la ultima clase de intro"))


'''
Reto 3
Entradas:
numeroEntero(int)
lista(str)
numero(int)
Salidas: cribaEratostenes(str)
Restricciones: numeroEntero(Debe ser un número entero positivo)
'''
def cribaEratostenes(pN):
    listaNumeros = list(range(2,pN+1))
    indice = 0
    listaoriginal = listaNumeros
    while listaNumeros[indice]**2<=pN:
        primo = listaNumeros[indice]

        for elemento in listaoriginal:
            if elemento % primo == 0 and elemento != primo:
                listaNumeros.remove(elemento)
        
        indice +=1
    return listaNumeros
print(cribaEratostenes(20))
    

