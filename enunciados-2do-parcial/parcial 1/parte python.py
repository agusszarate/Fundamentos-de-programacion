MAX_NUM = 50
MAX = str(50) + ',,,,'

def leer(archivo): 
    linea = archivo.readline()

    if(linea):
        linea = linea.strip()
    else:
        linea = MAX
    
    campo = linea.split(',')

    return (int(campo[0]), campo[1], campo[2], campo[3], campo[4])

def grabar(archivo, dia, equipo_local, goles_local, equipo_visitante, goles_visitante, copa): 
    archivo.write(str(dia) + ',' + equipo_local + ',' + goles_local + ',' + equipo_visitante + ',' + goles_visitante + ',' + copa + '\n')

def merge(euro_archivo, america_archivo, resultado_archivo):
    dia1, local1, goles_local1, visitante1, goles_visitante1 = leer(euro_archivo)
    dia2, local2, goles_local2, visitante2, goles_visitante2 = leer(america_archivo)

    while dia1 < MAX_NUM or dia2 < MAX_NUM:
        minimo = min(dia1, dia2)

        while dia1 == minimo:
            grabar(resultado_archivo, dia1, local1, goles_local1, visitante1, goles_visitante1, 'EUROCOPA')
            dia1, local1, goles_local1, visitante1, goles_visitante1 = leer(euro_archivo)
        
        while dia2 == minimo: 
            grabar(resultado_archivo, dia2, local2, goles_local2, visitante2, goles_visitante2, 'COPA AMERICA')
            dia2, local2, goles_local2, visitante2, goles_visitante2 = leer(america_archivo)

def analizar_archivo():
    eurocopa_archivo = open('eurocopa.txt', 'r')
    copa_america__archivo = open('copa_america.txt', 'r')
    resultado_archivo = open('resultado.txt', 'w')

    merge(eurocopa_archivo, copa_america__archivo, resultado_archivo)

    eurocopa_archivo.close()
    copa_america__archivo.close()
    resultado_archivo.close()

def armar_diccionario():

    diccionario = {}

    with open('resultado.txt', 'r') as resultados:
        for linea in resultados:
            linea = linea.strip()
            campo = linea.split(',')

            dia, equipo1, goles1, equipo2, goles2, copa = campo
            
            gano1 = int(goles1) > int(goles2)
            gano2 = int(goles1) < int(goles2)

            goles1 = int(goles1)
            goles2 = int(goles2)

            for equipo in [equipo1, equipo2]:
                if equipo not in diccionario.keys():
                    diccionario[equipo] = [0, 0, 0]

            if gano1:
                diccionario[equipo1][0] += 1
                diccionario[equipo2][2] += 1
            elif gano2:
                diccionario[equipo1][2] += 1
                diccionario[equipo2][0] += 2
            else:
                diccionario[equipo1][1] += 1
                diccionario[equipo2][1] += 1
     
    return diccionario

# def armar_listado(diccionario):
#     # Filtrar equipos con al menos una victoria
#     equipos_con_victorias = [(equipo, datos[0]) for equipo, datos in diccionario.items() if datos[0] > 0]
#     # Ordenar de mayor a menor por cantidad de partidos ganados
#     equipos_ordenados = sorted(equipos_con_victorias, key=lambda x: x[1], reverse=True)
#     # Imprimir el listado
#     print("País - Partidos Ganados")
#     for equipo, ganados in equipos_ordenados:
#         print(f"{equipo} - {ganados}")


def armar_listado(diccionario):
    equipos = [(equipo, dato[0]) for equipo, dato in diccionario.items() if dato[0] > 0]

    equipos_ordenados = sorted(equipos, key=lambda x: x[1], reverse=True)

    for equipo, resultado in equipos_ordenados:
        print(equipo + ', ' + str(resultado))
    
def main():
    analizar_archivo()

    historial_equipos = armar_diccionario()

    armar_listado(historial_equipos)

main()