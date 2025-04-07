def calcular_total_ventas(matriz_ventas: list) -> float:
    total = 0
    for sucursal in matriz_ventas:
        for venta_diaria in sucursal:
            total += venta_diaria
    return total


def encontrar_sucursal_menos_ventas(matriz_ventas: list) -> int:
    ventas_por_sucursal = []
    
    for sucursal in matriz_ventas:
        total_sucursal = sum(sucursal)
        ventas_por_sucursal.append(total_sucursal)
    
    return ventas_por_sucursal.index(min(ventas_por_sucursal))


def encontrar_dia_mayor_venta(matriz_ventas: list) -> tuple:
    # Inicializamos una lista para almacenar las ventas por día
    ventas_por_dia = [0] * 5
    
    for sucursal in matriz_ventas:
        for dia in range(5):
            ventas_por_dia[dia] += sucursal[dia]
    
    max_venta = max(ventas_por_dia)
    dia_max_venta = ventas_por_dia.index(max_venta)
    
    return (dia_max_venta, max_venta)


def imprimir_resultados(total_ventas: float, sucursal_menos_ventas: int, dia_mayor_venta: tuple):
    DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    print(f"a. Total semanal de ventas: ${total_ventas}")
    print(f"b. Sucursal que vendió menos: {sucursal_menos_ventas + 1}")
    print(f"c. Día que se vendió más: {DIAS[dia_mayor_venta[0]]}, "
          f"con un total de ${dia_mayor_venta[1]}")


def main():
    # Matriz de ventas: 3 sucursales x 5 días (lunes a viernes)
    # Cada fila representa una sucursal, cada columna un día
    matriz_ventas = [
        [1500.50, 2300.75, 1800.25, 2100.00, 2700.30],  # Sucursal 1
        [1200.80, 1900.20, 2100.50, 1700.40, 2200.10],  # Sucursal 2
        [1800.90, 2000.30, 1600.75, 2400.60, 1900.80],  # Sucursal 3
    ]
    
    # a. Calcular total semanal
    total_ventas = calcular_total_ventas(matriz_ventas)
    
    # b. Encontrar sucursal que vendió menos
    sucursal_menos_ventas = encontrar_sucursal_menos_ventas(matriz_ventas)
    
    # c. Encontrar día que se vendió más
    dia_mayor_venta = encontrar_dia_mayor_venta(matriz_ventas)
    
    # Imprimir resultados
    imprimir_resultados(total_ventas, sucursal_menos_ventas, dia_mayor_venta)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()