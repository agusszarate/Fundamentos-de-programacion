#include <stdio.h>
#include <stdbool.h>

bool es_binario(int numero) {

    bool respuesta = false;

    if (numero == 0 || numero == 1){
        respuesta = true;
    }else {

        int ultimo_digito = numero % 10;

        if (ultimo_digito == 1 || ultimo_digito == 0){
            int anterior = (numero - ultimo_digito) / 10;
            respuesta = es_binario(anterior);
        }
    }

    return respuesta;
}

int main () {
    printf("101 es binario: %s\n", es_binario(101) ? "true" : "false");
    
    printf("2 es binario: %s\n", es_binario(2) ? "true" : "false");
    
    printf("20 es binario: %s\n", es_binario(20) ? "true" : "false");
    
    printf("1 es binario: %s\n", es_binario(1) ? "true" : "false");
    
    printf("0 es binario: %s\n", es_binario(0) ? "true" : "false");
    
    printf("100000 es binario: %s\n", es_binario(100000) ? "true" : "false");
    
    printf("100009 es binario: %s\n", es_binario(100009) ? "true" : "false");

}