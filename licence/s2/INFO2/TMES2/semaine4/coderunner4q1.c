#include <stdio.h>

void conversion(int tabF[], float tabC[], int nb) {
    for (int i =0; i <nb; i++){
        tabC[i]= (tabF[i]-32)*((5)/(9*1.0));
    }
}

int main() {
   int tabF[31];
   float tabC[31];
   int i, nb;

   scanf("%d", &nb);
   for (i = 0; i < nb; i++) {
      scanf("%d", &tabF[i]);
   }

   conversion(tabF, tabC, nb);
   for (i = 0; i < nb; i++) {
      printf("%.1f  ", tabC[i]);
   }
   printf("\n");
   return 0;
}
