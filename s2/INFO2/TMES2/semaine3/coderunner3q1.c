#include <stdio.h>

#define NB_VALEURS 6
int pos = 0;
int neg = 0;
int zeros = 0;

void pos_neg_zero(int val) {
    if (val>0) {
        pos++;
    }
    else if (val<0){
        neg++;
    }
    else { zeros++;
    }
}

int main(){
   int i, val;
   printf("Saisissez une suite de %d valeurs\n", NB_VALEURS);
   for (i = 0; i < NB_VALEURS; i++) {
      scanf("%d", &val);
      pos_neg_zero(val);
   }

   printf("%d valeurs negatives, %d valeurs positives, %d valeurs nulles.\n", neg,pos,zeros);
   return 0;
}
