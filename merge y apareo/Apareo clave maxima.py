"""
Se tienen los resultados de la Eurocopa y la Copa América en dos archivos de texto  con formato csv,
llamados eurocopa.csv y copa_america.csv. Estos archivos tienen en cada linea, el resultado de un partido.
Los campos son:

    dia, equipo_local, goles_local, equipo_visitante, goles_visitante

Los archivos se guardaron en forma secuencial, comenzando desde el dia 1 del campeonato, por lo que están ordenados por dia.


Ejemplo

    1,Alemania,5,Escocia,1
    2,Hungria,1,Suiza,3
    2,Espania,3,Croacia,0
    2,Italia,2,Albania,2
    etc

Se pide realizar un programa modular (compuesto por funciones) en python que:

1) 
Recorriendo una sola vez los dos archivos y sin cargarlos completamente en memoria, los unifique (merge con clave máxima) en un único archivo ordenado por dia,
manteniendo el orden original y agregando un campo que indique de que archivo es la linea que se está escribiendo (EUROCOPA o COPA_AMERICA), 
ante igualdad del dia, guardar en primer lugar los de Eurocopa.


"""

MAX_DIA = 50
MAX = str(MAX_DIA) + ",,,,"

def leer(archivo):
    linea = archivo.readline()
    if (linea):
        linea = linea.rstrip()
    else:
        linea = MAX

    campos = linea.split(',')
    return (int(campos[0]),) + tuple([campos[i] for i in range(1, len(campos))])    


def guardar(dia, eq_local, gol_local, eq_vis, gol_vis, torneo, archivo):
    archivo.write(str(dia) + "," + eq_local + "," + gol_local + "," + eq_vis + "," + gol_vis + "," + torneo + "\n")

def mezcla(torneo1, torneo2, unificado):
  
  # Lectura inicial de ambas fuentes de origen
  dia1, eq_local1, gol_local1, eq_vis1, gol_vis1 = leer(torneo1)
  dia2, eq_local2, gol_local2, eq_vis2, gol_vis2 = leer(torneo2)
      
  # Mientras alguno de los dos contenga información
  while (dia1 < MAX_DIA) or (dia2 < MAX_DIA):
    minimo = min(dia1, dia2)
            
    while (dia1 == minimo):
      guardar(dia1, eq_local1, gol_local1, eq_vis1, gol_vis1, "EUROCOPA", unificado)
      dia1, eq_local1, gol_local1, eq_vis1, gol_vis1 = leer(torneo1)
		
    while (dia2 == minimo):
      guardar(dia2, eq_local2, gol_local2, eq_vis2, gol_vis2, "COPA_AMERICA", unificado)
      dia2, eq_local2, gol_local2, eq_vis2, gol_vis2 = leer(torneo2)


def unificar():
    eurocopa = open('eurocopa.csv', 'r')
    copa_america = open('copa_america.csv', 'r')
    union = open('unionx.csv', 'w')

    mezcla(eurocopa, copa_america, union)
    
    eurocopa.close()
    copa_america.close()
    union.close()

def main():
    unificar()

main()