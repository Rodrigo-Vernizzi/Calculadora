#include <stdio.h>


int main()
{
  int m, n, p, q, c, d, k, sum = 0;
  int matriz1[10][10], matriz2[10][10], matriz3[10][10];

  printf("Digite o numero de linhas e colunas da primeira matriz\n");
  scanf("%i%i", &m, &n);
  printf("Digite os elementos da primeira matriz\n");

  for (c = 0; c < m; c++)
    for (d = 0; d < n; d++)
      scanf("%i", &matriz1[c][d]);

  printf("Digite o numero de linhas e colunas da segunda matriz\n");
  scanf("%i%i", &p, &q);

  if (n != p)
    printf("Nao e possivel multiplica-las.\n");
  else
  {
    printf("Digite  os elementos da segunda matriz\n");

    for (c = 0; c < p; c++)
      for (d = 0; d < q; d++)
        scanf("%i", &matriz2[c][d]);

    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++) {
        for (k = 0; k < p; k++) {
          sum = sum + matriz1[c][k]*matriz2[k][d];
        }

       matriz3[c][d] = sum;
        sum = 0;
      }
    }

    printf("A multiplicacao dessas matrizes resulta em:\n");

    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%i\t", matriz3[c][d]);

      printf("\n");
    }
  }

  return 0;
}
