"""
Se tienen dos archivos, uno llamadado productos.csv (archivo maestro) y otro llamado productos-act.csv (archivo con actualizaciones)

A partir de estos dos archivos se debe generar un nuevo archivo maestro actualizado.
Si hay una actualización de un producto prevalecen los datos de la actualización, 
en el caso que el precio actualizado sea cero, se debe conservar el precio anterior.
En el caso de existir actualización será única por producto.

Ejemplo archivo maestro:
id_producto,precio_unitario,stock_deseado,stock_actual
1042,12.3,12,24
1142,22.0,60,90
1242,21.3,10,20
1342,54.3,5,10
1442,65.3,12,50
1542,76.2,2,5

Ejemplo archivo actualización:
id_producto,precio_unitario,stock_deseado,stock_actual
1042,0,12,24
1442,65.3,100,50
1542,40.2,2,5

Se pide realizar un programa modular (compuesto por funciones) en python que:

1) 
Recorriendo una sola vez los dos archivos y sin cargarlos completamente en memoria, los unifique en un único archivo ordenado por id_producto,
manteniendo el orden original y con las actualizaciones solicitadas.

Pueden existir actulizaciones que no existan en el maestro, en este caso registrarlo en un archivo de texto errores.txt
"""

ID_PRODUCTO_INVALIDO = 0
MAX = str(ID_PRODUCTO_INVALIDO) + ",,,"

def ignorar_linea(archivo):
	archivo.readline()

def leer(archivo):
	linea = archivo.readline()
	if (linea):
		linea = linea.rstrip()
	else:
		linea = MAX

	campos = linea.split(',')
	return (int(campos[0]),) + tuple([campos[i] for i in range(1, len(campos))])    

def guardar(id_producto, precio_unitario, stock_deseado, stock_actual, archivo):
	archivo.write(str(id_producto) + "," + precio_unitario + "," + stock_deseado + "," + stock_actual + "\n")

def guardar_error(id_producto, archivo):
	archivo.write(str(id_producto) + "\n")

def mezcla(productos, actualizacion, unificado):
	errores = open('errores.txt', 'w')

	# Ignoramos cabeceras
	ignorar_linea(productos)
	ignorar_linea(actualizacion)

  	# Lectura inicial de ambas fuentes de origen
	id_producto, precio_unitario, stock_deseado, stock_actual = leer(productos)
	id_producto_act, precio_unitario_act, stock_deseado_act, stock_actual_act = leer(actualizacion)
	  
	# Mientras alguno de los dos contenga información
	while (id_producto != ID_PRODUCTO_INVALIDO) and (id_producto != ID_PRODUCTO_INVALIDO):
		
		if (id_producto == id_producto_act):
			precio = precio_unitario if (precio_unitario_act == "0") else precio_unitario_act
			guardar(id_producto, precio, stock_deseado_act, stock_actual_act, unificado)
			id_producto, precio_unitario, stock_deseado, stock_actual = leer(productos)
			id_producto_act, precio_unitario_act, stock_deseado_act, stock_actual_act = leer(actualizacion)
		elif (id_producto < id_producto_act):
			guardar(id_producto, precio_unitario, stock_deseado, stock_actual, unificado)
			id_producto, precio_unitario, stock_deseado, stock_actual = leer(productos)
		else:
			guardar_error(id_producto_act, errores)
			id_producto_act, precio_unitario_act, stock_deseado_act, stock_actual_act = leer(actualizacion)

	while (id_producto != ID_PRODUCTO_INVALIDO):
		guardar(id_producto, precio_unitario, stock_deseado, stock_actual, unificado)
		id_producto, precio_unitario, stock_deseado, stock_actual = leer(productos)

	while (id_producto_act != ID_PRODUCTO_INVALIDO):
		guardar_error(id_producto_act, errores)
		id_producto_act, precio_unitario_act, stock_deseado_act, stock_actual_act = leer(actualizacion)
	
	errores.close()


def unificar():
	maestro = open('productos.csv', 'r')
	actualizacion = open('productos-act.csv', 'r')
	union = open('unionx.csv', 'w')

	mezcla(maestro, actualizacion, union)
	
	maestro.close()
	actualizacion.close()
	union.close()

def main():
	unificar()

main()