/*
Considerando la potencia de numeros reales con exponentes enteros mayores o iguales a cero.

Definición recursivade de la función:

potencia(x, n)

potenia(x, n) =   1                     si n = 0 (caso base)
                  x * potencia(x, n-1)  si n > 0 (caso recursivo)
*/

#include <stdio.h>

typedef struct {
  float base;
  int exp;
} t_calculo;

float potencia(float base, int exponente)
{
  if (exponente == 0)
    // caso base
    return 1;
  // caso recursivo            
  return base * potencia(base, exponente-1);   
}

int main()
{
  // creación de diferentes casos de prueba
  t_calculo calculos[] = {
    {2.0, 0},
    {2.0, 1},
    {2.0, 2},
    {2.0, 3}
  };
  int i, ml = sizeof(calculos) / sizeof(t_calculo);

  // ejecución de los calculos de prueba
  for (i=0; i<ml; i++) {
    printf("%.2f a la potencia de %d es %.2f\n\n", calculos[i].base, calculos[i].exp, potencia(calculos[i].base, calculos[i].exp));
  }

  return 0;
}
