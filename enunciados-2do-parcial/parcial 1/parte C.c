#include <stdio.h>
#include <stdbool.h>

int pertenece(int vec[], int n, int valor){
    int resultado = 0;

    if (n != -1){
        if(vec[n-1] == valor) {
            resultado = 1;
        } else {
            resultado = pertenece(vec, n-1, valor);
        }
    }

    return resultado;
}

int main() {
    int vec[] = {1,2,3,4,5,6};
    printf("Valor %d", pertenece(vec, 6, 6));
    return 0;
}