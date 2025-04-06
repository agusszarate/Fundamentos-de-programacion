"""
Pruebas unitarias para las funciones del programa de análisis de ventas.
Verifica las funcionalidades básicas y las decisiones de implementación.
"""
import unittest
from main import calcular_total_ventas, encontrar_sucursal_menos_ventas, encontrar_dia_mayor_venta


class TestVentas(unittest.TestCase):
    """Clase de pruebas para funciones de análisis de ventas."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Matriz de prueba base: 3 sucursales x 5 días
        self.matriz_test = [
            [1500.50, 2300.75, 1800.25, 2100.00, 2700.30],  # Sucursal 1
            [1200.80, 1900.20, 2100.50, 1700.40, 2200.10],  # Sucursal 2
            [1800.90, 2000.30, 1600.75, 2400.60, 1900.80],  # Sucursal 3
        ]
        
        # Matriz con valores iguales para probar empates
        self.matriz_empate = [
            [1000.00, 1000.00, 1000.00, 1000.00, 1000.00],  # Sucursal 1
            [1000.00, 1000.00, 1000.00, 1000.00, 1000.00],  # Sucursal 2
            [1000.00, 1000.00, 1000.00, 1000.00, 1000.00],  # Sucursal 3
        ]
        
        # Matriz con valores negativos (caso de devoluciones o ajustes)
        self.matriz_negativos = [
            [1500.50, -300.75, 1800.25, 2100.00, 2700.30],  # Sucursal 1
            [1200.80, 1900.20, -500.50, 1700.40, 2200.10],  # Sucursal 2
            [-800.90, 2000.30, 1600.75, 2400.60, 1900.80],  # Sucursal 3
        ]

    def test_total_ventas(self):
        """Prueba el cálculo correcto del total de ventas."""
        total_esperado = sum(sum(sucursal) for sucursal in self.matriz_test)
        self.assertEqual(calcular_total_ventas(self.matriz_test), total_esperado)
        
        # Prueba con matriz que tiene valores negativos
        total_esperado_neg = sum(sum(sucursal) for sucursal in self.matriz_negativos)
        self.assertEqual(calcular_total_ventas(self.matriz_negativos), total_esperado_neg)

    def test_sucursal_menos_ventas(self):
        """
        Prueba la identificación de la sucursal con menos ventas.
        Decisión no aclarada: En caso de empate, se devuelve la primera sucursal encontrada.
        """
        # La sucursal 1 (índice 0) tiene el total más bajo
        self.assertEqual(encontrar_sucursal_menos_ventas([
            [100, 100, 100, 100, 100],  # Total: 500
            [200, 200, 200, 200, 200],  # Total: 1000
            [300, 300, 300, 300, 300]   # Total: 1500
        ]), 0)
        
        # Prueba con empate: debe devolver el primer índice encontrado
        self.assertEqual(encontrar_sucursal_menos_ventas(self.matriz_empate), 0)

    def test_dia_mayor_venta(self):
        """
        Prueba la identificación del día con mayor venta.
        Decisión no aclarada: En caso de empate, se devuelve el primer día encontrado.
        """
        # En la matriz de prueba, el día con más ventas es el viernes (índice 4)
        dia, monto = encontrar_dia_mayor_venta(self.matriz_test)
        self.assertEqual(dia, 4)  # Viernes
        
        # El monto debe ser la suma de todas las ventas de ese día
        monto_esperado = sum(sucursal[4] for sucursal in self.matriz_test)
        self.assertEqual(monto, monto_esperado)
        
        # Prueba con empate: debe devolver el primer día encontrado
        dia_empate, monto_empate = encontrar_dia_mayor_venta(self.matriz_empate)
        self.assertEqual(dia_empate, 0)  # Lunes (primer día)
        self.assertEqual(monto_empate, 3000.0)  # 1000 * 3 sucursales

    def test_con_valores_negativos(self):
        """
        Prueba el comportamiento con valores negativos (posibles devoluciones).
        Decisión no aclarada: Se permiten valores negativos en las ventas.
        """
        # Verificar que la sucursal 2 es la que menos vendió (por el valor negativo)
        sucursal_con_menor_venta = encontrar_sucursal_menos_ventas([
            [1000, 1000, 1000, 1000, 1000],   # Total: 5000
            [-2000, 1000, 1000, 1000, -2000], # Total: -1000
            [1000, 1000, 1000, 1000, 1000]    # Total: 5000
        ])
        self.assertEqual(sucursal_con_menor_venta, 1)
        
        # Verificar que se identifica correctamente el día con mayor venta
        dia_mayor, monto = encontrar_dia_mayor_venta(self.matriz_negativos)
        # El día con mayor venta debería ser el jueves (índice 3)
        self.assertEqual(dia_mayor, 3)


if __name__ == '__main__':
    unittest.main()