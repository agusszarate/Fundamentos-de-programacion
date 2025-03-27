def calcular_mcd(primer_numero: int, segundo_numero: int) -> int:
    """
    Calcula el máximo común divisor de dos números usando el algoritmo de Euclides.
    
    Parámetros:
    primer_numero (int): Primer número entero.
    segundo_numero (int): Segundo número entero.
    
    Retorna:
    int: El máximo común divisor de primer_numero y segundo_numero.
    """
    primer_numero_abs = abs(primer_numero)
    segundo_numero_abs = abs(segundo_numero)
    
    while segundo_numero_abs != 0:
        numero_temporal = segundo_numero_abs
        segundo_numero_abs = primer_numero_abs % segundo_numero_abs
        primer_numero_abs = numero_temporal
    
    resultado = primer_numero_abs
    
    return resultado


def calcular_mcm(primer_numero: int, segundo_numero: int) -> int:
    """
    Calcula el mínimo común múltiplo de dos números.
    
    Parámetros:
    primer_numero (int): Primer número entero.
    segundo_numero (int): Segundo número entero.
    
    Retorna:
    int: El mínimo común múltiplo de primer_numero y segundo_numero.
    """
    primer_numero_abs = abs(primer_numero)
    segundo_numero_abs = abs(segundo_numero)
    
    if primer_numero_abs == 0 or segundo_numero_abs == 0:
        resultado = 0
    else:
        mcd_resultado = calcular_mcd(primer_numero_abs, segundo_numero_abs)
        resultado = (primer_numero_abs // mcd_resultado) * segundo_numero_abs
    
    return resultado


def calcular_mcm_en_rango(primer_numero: int, segundo_numero: int, primer_limite: int, segundo_limite: int) -> int:
    
    # Se calcula el MCD de los dos números usando el algoritmo de Euclides.

    primer_numero_abs = abs(primer_numero)
    segundo_numero_abs = abs(segundo_numero)
    
    primer_numero_mcd = primer_numero_abs
    segundo_numero_mcd = segundo_numero_abs

    while segundo_numero_mcd != 0:
        numero_temporal = segundo_numero_mcd
        segundo_numero_mcd = primer_numero_mcd % segundo_numero_mcd
        primer_numero_mcd = numero_temporal
    
    resultado_mcd = primer_numero_mcd

    # Se calcula el MCM de los dos números.
    resultado_mcm = (primer_numero_abs // resultado_mcd) * segundo_numero_abs
    
    # Se determina si el MCM se encuentra dentro del rango especificado.
    limite_inferior = min(primer_limite, segundo_limite)
    limite_superior = max(primer_limite, segundo_limite)
    
    if limite_inferior <= resultado_mcm <= limite_superior:
        resultado = resultado_mcm
    else:
        resultado = 0
    
    return resultado

valor = calcular_mcm_en_rango(-1032, -180, 999999990, 10)

print(valor)