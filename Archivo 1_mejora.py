
'''
Reto 1 
Entradas: pNum (int)
Salidas True si pNum convertido a binario es palindromo, False si pNum convertido a binario no es palindromo / numeroBinario (int)
Restricciones: pNum > 0
'''
def convertirABinario(pNum):
    return int(bin(pNum)[2:])
print(convertirABinario(17))

def esPalindromo(pNum):
    numeroInvertido = 0
    numero = pNum
    while (numero > 0):
        numeroInvertido = (numeroInvertido * 10) + (numero % 10)
        numero = numero // 10
    if (numeroInvertido == pNum):
        return True
    else: 
        return False

def determinarBinarioPalindromo(pNum):
    if esPalindromo(convertirABinario(pNum)) == True:
        return True
    else: 
        return False
    
print(determinarBinarioPalindromo(17))

'''
Reto 2 
Entradas: Y (int)
Salidas: newtonRaphson (float)
Restricciones: pNum > 0
'''

def calcularValorAbsoluto(pNum):
    if (pNum >= 0):
        return pNum
    else:
        return -pNum

def calcularNewtonRaphson(Y):
    x = 1
    tolerancia = 0.0001
    while calcularValorAbsoluto(Y-(x**2)) >= tolerancia:
        x = 1/2 * (x + (Y / x))
    return x
print(calcularNewtonRaphson(9))

