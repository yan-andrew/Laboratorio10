
'''
Reto 1
Entradas: monto(int)
Salidas: desglosarBilletes(str)
Restricciones: monto(Debe ser un número entero positivo) 
'''
def desglosarBilletesAuxiliar(monto, validador):
    if(validador == 0):
        cantidad = monto//20000
        lista, cantidadBilletes = desglosarBilletesAuxiliar(monto-(20000*cantidad), validador+1)
        if(cantidadBilletes+cantidad > 15):
            return -1
        else:
            return [[cantidad, 20000]]+lista
    
    if(validador == 1):
        cantidad = monto//10000
        lista, cantidadBilletes = desglosarBilletesAuxiliar(monto-(10000*cantidad), validador+1)
        return [[cantidad, 10000]]+lista, cantidadBilletes+cantidad
    
    if(validador == 2):
        cantidad = monto//5000
        lista, cantidadBilletes = desglosarBilletesAuxiliar(monto-(5000*cantidad), validador+1)
        return [[cantidad, 5000]]+lista, cantidadBilletes+cantidad
    
    if(validador == 3):
        cantidad = monto//2000
        lista, cantidadBilletes = desglosarBilletesAuxiliar(monto-(2000*cantidad), validador+1)
        return [[cantidad, 2000]]+lista, cantidadBilletes+cantidad
    
    if(validador == 4):
        cantidad = monto//1000
        return [[cantidad, 1000]],cantidad


def desglosarBilletes(monto):
    if(monto%1000 != 0):
        return -1
    return desglosarBilletesAuxiliar(monto, 0)
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
    

