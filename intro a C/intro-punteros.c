#include <stdio.h>
int main()
{
    /*
    * Declaramos 2 variables, una de tipo int y
    * una de tipo int* (puntero a entero)
    */
    int var1, *p_entero;

    /* Inicializo variables */
    p_entero = NULL;
    var1 = 5;

    printf("var1: %d \n", var1); /* var1: 5 */

    /* Asigno a p_entero la dirección de memoria de var1 */
    p_entero = &var1;

    /* Modificamos el valor de var1 a través del puntero */
    *p_entero = 20;

    printf("var1: %d \n", var1); /* var1: 20 */
    printf("Valor de var1 desreferenciando p_entero: %d \n", *p_entero);
    
    /*
    * Podemos conocer las direcciones de memoria involucradas
    * Utilizamos el formateador %p para mostrar direcciones
    * de memoria en notación hexadecimal.
    */
    printf("Dirección de var1: %p\n", &var1);
    printf("Dirección de p_entero: %p\n", &p_entero);
    printf("Dirección de *p_entero: %p\n", p_entero);
    return 0;
}