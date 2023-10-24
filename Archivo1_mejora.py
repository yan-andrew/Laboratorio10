
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
    pNum = str(pNum)
    indice = 0
    indice_negativo = -1
    while (indice < len(pNum) // 2):
        if (pNum[indice] != pNum[indice_negativo]):
            return False
        indice += 1
        indice_negativo -= 1
    return True

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

