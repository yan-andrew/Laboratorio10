
#Reto 01

'''
Entradas:
- resultado (int)
- pListaB (list)
Salidas:
- subLista (list)
Restricciones:
- la funcion no valida restricciones
- pListaB != []
'''

def validarSublista (resultado, pListaB):
    indiceB = 0
    subLista = []
    while (indiceB != len(pListaB)):
        if (resultado == pListaB[indiceB]):
            subLista.append(0)
        elif (resultado > pListaB[indiceB]):
            subLista.append(resultado)
        elif (resultado < pListaB[indiceB]):
            subLista.append(pListaB[indiceB])
        indiceB += 1
    return subLista

'''
Entradas:
- pListaA (list)
- pLista (list)
Salidas:
- sublistasOperadas (list)
Restricciones:
- la funcion no valida restricciones
- pListaA != []
- pListaB != []
'''

def aplicarOperacionesSublista(pListaA, pListaB):
    indiceA = 0
    sublistasOperadas = []
    while (indiceA != len(pListaA)):
        if (pListaA == [] or pListaB == []):
            sublistasOperadas = []
        subLista = pListaA[indiceA]
        if (subLista[1] == "+"):
            resultado = subLista[0] + subLista[2]
        elif (subLista[1] == "-"):
            resultado = subLista[0] - subLista[2]
        elif (subLista[1] == "/"):
            resultado = subLista[0] / subLista[2]
        elif (subLista[1] == "*"):
            resultado = subLista[0] * subLista[2]
        elif (subLista[1] != "+""-""*""/"):
            return "Las operaciones válidas son ‘+’, ‘-’, ‘*’, ‘/’"
        sublistasOperadas += [validarSublista(resultado, pListaB)]
        indiceA += 1
    return sublistasOperadas
#print (aplicarOperacionesSublista([[4, "*", 4],[8, "-", 1]], [5, 9, 16]))
#print(aplicarOperacionesSublista([], [5, 9, 16]))
#print(aplicarOperacionesSublista([[4, "+", 4],[8, "%", 1]], [5, 9, 16]))

#Reto 02

'''
Entradas:
- pNum (int)
Salidas:
- suma (int)
Restricciones:
- la funcion no valida restricciones
- pNum > 0
'''

def sumaDivisores(pNum):
    suma = 1
    for i in range(2, int(pNum**0.5) + 1):
        if pNum % i == 0:
            suma += i
            if i != pNum // i: 
                suma += pNum // i
    return suma

'''
Entradas:
- pNum (int)
Salidas:
- listaNumerosAmigos (list)
Restricciones:
- la funcion no valida restricciones
- pNum > 0
'''

def encontrarNumerosAmigos(pNum):
    lista = []
    for n in range(2, pNum):
        numeroB = sumaDivisores(n)
        if (numeroB < n):
            if (sumaDivisores(numeroB) == n):
                lista.append(numeroB)
                lista.append(n)
    listaNumerosAmigos = [lista[i:i + 2] for i in range(0, len(lista), 2)]
    return listaNumerosAmigos

#print (encontrarNumerosAmigos(1220))
#print (encontrarNumerosAmigos(3000))
#print (encontrarNumerosAmigos(10900))

#Reto 03

'''
Entradas:
- pListaA (list)
- pListaB (list)
Salidas:
- nuevaLista (list)
Restricciones:
- La función no valida restricciones
- pListaA de la forma [[elemento1, elemento2, n], [elemento1, elemento2, n] , … ]
'''

def triosListas(plistaA,plistaB):
    n = 1
    nuevaLista = []
    subListaA = plistaA[0]
    subListaB = plistaA[1]
    for i in plistaB:
        if (subListaA[0] == i):
            while (subListaA[2] >= n):
                nuevaLista.append(subListaA[1])
                n += 1
            n = 1
        else: 
            if (subListaB[0] == i):
                while (subListaB[2] >= n):
                    nuevaLista.append(subListaB[1])
                    n +=1
                n = 1
            else:
                nuevaLista.append(i)
    return nuevaLista

print(triosListas([["s",  "z",  2], ["a",  "i",  4]],["e",  "s",  "p",  "a", "ñ",  "a"] ))
print(triosListas([["a",  "e",  2], ["m",  "p",  3]] , ["m",  "a",  "m",  "a"]))
print(triosListas([["t",  "t",  1], ["e",  "e",  1]] , ["k",  "e",  "n",  "n", "e",  "t", "h"])) 