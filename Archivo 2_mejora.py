
'''
Función 1: Total de ataques enviados a nivel mundial
Entradas: lista(list)
Salidas: totalAtaquesMundiales(int)
Restricciones: cadena != ""
'''
def totalAtaquesMundialEnviados(lista):
    indice = 4
    totalAtaquesMundiales = 0
    while(indice < len(lista)):
        ataque = ''
        for x in lista[indice]:
            if x != " ":
                ataque += x
            else:
                break
        totalAtaquesMundiales += int(ataque)
        indice += 4
    return totalAtaquesMundiales
print(totalAtaquesMundialEnviados(['Costa Rica','Malware','Abr-2022','620','11 Costa Rica','Ransomware','Abr-2022','709','210 Estados Unidos','Denegación de servicios','Mar-2022','7800','4521 Rusia','Spyware','Mar-2022','645','1890']))
print(totalAtaquesMundialEnviados(['Bélgica','Phishing','Abr-2022','1640','5390 China','Ransomware', 'Abr-2022','41457','21680 México','Phishing','Abr-2022','4637','4589 Estados Unidos','Malware','Abr-2022','52800','45213 Brasil','Exploit','Mar-2022','645','1890 China','Phishing','Abr-2022','78165','76455']))

'''
Función 2: Total de ataques enviados desde un país. 
Entradas: 
- cadena(str)
- pais(str)
Salidas: totalAtaquesDesdePais(int)
Restricciones: cadena != ""
'''

def totalAtaquesEnviadosDesdePaís(lista,pais):
    indice = 0
    totalAtaquesDesdePais = 0
    while(indice < len(lista)):
        ataque = '0'
        if (pais in lista[indice]):
            try:
                for x in lista[indice]:
                    if type(int(x)) == int:
                        ataque += x
            except:
                None
        totalAtaquesDesdePais += int(ataque)
        indice += 1
    return  totalAtaquesDesdePais
print(totalAtaquesEnviadosDesdePaís(['Costa Rica','Malware','Abr-2022','620','11 Costa Rica','Ransomware','Abr-2022,709','210 Estados Unidos','Denegación de servicios','Mar-2022','7800','4521' 'Rusia','Spyware','Mar-2022','645','1890'], "Costa Rica"))
print(totalAtaquesEnviadosDesdePaís(['Bélgica','Phishing','Abr-2022','1640','5390 China','Ransomware','Abr-2022','41457','21680 México','Phishing','Abr-2022','4637','4589 Estados Unidos','Malware','Abr-2022','52800','45213 Brasil','Exploit','Mar-2022','645','1890 China','Phishing','Abr-2022','78165','76455'],"Ucrania"))
print(totalAtaquesEnviadosDesdePaís(['Bélgica','Phishing','Abr-2022','1640','5390 China','Ransomware','Abr-2022','41457','21680 México','Phishing','Abr-2022','4637','4589', 'Estados Unidos','Malware','Abr-2022','52800','45213 Brasil','Exploit','Mar-2022','645','1890 China','Phishing','Abr-2022','78165','76455'], "China"))


'''
Función 3: El país con más ataques recibidos en un mes y año particular
Entradas: 
- cadena(str)
- fecha(str)
Salidas: paisConMayorAtaques(str) 
Restricciones: cadena != ""
'''
def paisMasAtaquesRecibidos(cadena, fecha):
    partes = cadena.split(',') 
    mayorAtaques = 0
    indice = 2
    pais_mas_atacado = ''

    while (indice < len(partes)):
        if (partes[indice] == fecha):
            paisMayorAtaques = ""
            indice2 = 0
            for x in partes[indice+2]:
                if x != " ":
                    indice2 += 1
                    paisMayorAtaques += x
                else:
                    break
            pais_atual = int(paisMayorAtaques)
            if (pais_atual > mayorAtaques):
                mayorAtaques = pais_atual
                pais_mas_atacado = partes[indice-2][indice2:]
        indice += 4

    return pais_mas_atacado

print(paisMasAtaquesRecibidos("Costa Rica,Malware,Abr-2022,620,11 Costa Rica,Ransomware,Abr-2022,709,210 Estados Unidos,Denegación de servicios,Mar-2022,7800,4521 Rusia,Spyware,Mar-2022,645,1890 ","Mar-2022"))
print(paisMasAtaquesRecibidos("Bélgica,Phishing,Abr-2022,1640,5390 China,Ransomware,Abr-2022,41457,21680 México,Phishing,Abr-2022,4637,4589 Estados Unidos,Malware,Abr-2022,52800,45213 Brasil,Exploit,Abr-2022,645,1890 China,Phishing,Abr-2022,78165,76455","Abr-2022"))