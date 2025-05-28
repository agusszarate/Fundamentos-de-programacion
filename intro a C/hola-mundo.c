#include <stdio.h>

unsigned long long factorial(int n) {
    unsigned long long resultado = 1;
    for (int i = 1; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

void main() {
    int numero;
    bool es_numero_valido = true;
    
    while (es_numero_valido){
        printf("Introduce un numero entero no negativo entre 0 y 20: ");
        scanf("%i", &numero);
        if (numero < 0 || numero > 20) {
            printf("El numero tiene que estar entre 0 y 20\n");
        } else {
            unsigned long long fact = factorial(numero);
            printf("El factorial de %d es %llu\n", numero, fact);
            es_numero_valido = false;
        }
    }
}