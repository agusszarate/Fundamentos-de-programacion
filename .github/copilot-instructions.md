# GitHub Copilot Instructions

## Configuración para Python

GitHub Copilot debe seguir las siguientes reglas al generar código en Python:

1. **Cumplimiento con PEP 8**: El código generado debe seguir las convenciones de estilo establecidas en PEP 8, a menos que se indique lo contrario en el archivo `pep.txt`.
2. **Reglas personalizadas**: Se deben aplicar las reglas definidas en el archivo `pep.txt`, las cuales tienen prioridad sobre PEP 8.
3. **Legibilidad y buenas prácticas**:
   - Usar nombres de variables y funciones descriptivos.
   - Aplicar `type hints` cuando sea posible.
   - Evitar código redundante o innecesariamente complejo.
4. **Estructura del código**:
   - Mantener una estructura clara y modular.
   - Aplicar la convención de nombres en `snake_case` para funciones y variables.
   - Usar `UpperCamelCase` para clases.

## Referencia al Archivo `pep.txt`

El archivo `pep.txt` contiene reglas adicionales o modificaciones a PEP 8. Copilot debe dar prioridad a estas reglas y aplicarlas en la generación de código.
