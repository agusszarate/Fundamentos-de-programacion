MAX = 50

def leer(archivo): 
    linea = archivo.readline()

    if(linea):
        linea = linea.rstrip()
    else: 
        linea = str(MAX) + ',,,,'

    campo = linea.split(',')

    return (int(campo[0]), campo[1], campo[2], campo[3], campo[4])

def guardar(archivo, dia, local, goles_local, visitante, goles_visitante, copa):
    archivo.write(str(dia) + ',' + local + ',' + goles_local + ',' + visitante + ',' + goles_visitante + ',' + copa + '\n')

def unificar(euro_archivo, america_archivo, resultado_archivo): 
    dia1, local1, goles_local1, visitante1, goles_visitante1 = leer(euro_archivo)
    dia2, local2, goles_local2, visitante2, goles_visitante2 = leer(america_archivo)

    while dia1 < MAX or dia2 < MAX: 
        menor = min(dia1, dia2)

        while dia1 == menor:
            guardar(resultado_archivo, dia1, local1, goles_local1, visitante1, goles_visitante1, 'EUROCOPA')
            dia1, local1, goles_local1, visitante1, goles_visitante1 = leer(euro_archivo)
        
        while dia2 == menor:
            guardar(resultado_archivo, dia2, local2, goles_local2, visitante2, goles_visitante2, 'COPA AMERICA')
            dia2, local2, goles_local2, visitante2, goles_visitante2 = leer(america_archivo)
        


def generar_resultados():
    eurocopa_archivo = open('eurocopa.txt', 'r')
    america_archivo = open('copa_america.txt', 'r')
    resultado_archivo = open('resultado.txt', 'w')

    unificar(eurocopa_archivo, america_archivo, resultado_archivo)

    eurocopa_archivo.close()
    america_archivo.close()
    resultado_archivo.close()

def generar_diccionario():
    diccionario = {}

    with open('resultado.txt', 'r') as resultados:
        for resultado in resultados:
            dia, local, goles_local, visitante, goles_visitante, copa = resultado.split(',')

            for equipo in (local, visitante):
                if equipo not in diccionario.keys():
                    diccionario[equipo] = [0, 0, 0]

            if int(goles_local) == int(goles_visitante):
                diccionario[local][1] += 1
                diccionario[visitante][1] += 1
            elif int(goles_local > goles_visitante):
                diccionario[local][0] += 1
                diccionario[visitante][2] += 1
            else:
                diccionario[local][2] += 1
                diccionario[visitante][0] += 1
    
    return diccionario

def generar_listado(diccionario):
    dic_filtrado = ([equipo, datos[0]] for equipo, datos in diccionario.items() if datos[0] >= 1)

    lista_ordenada = sorted(dic_filtrado, key=lambda x: x[1], reverse=True)

    for info in lista_ordenada:
        print(info[0], info[1])



def main():
    generar_resultados()

    dic = generar_diccionario()

    generar_listado(dic)


main()