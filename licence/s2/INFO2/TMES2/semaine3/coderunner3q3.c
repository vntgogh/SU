#include <stdio.h>

void min_max(int x, int *pmin, int *pmax) {
  if (x<=*pmin){
    *pmin=x;
  }
  else if (*pmax<= x){
    *pmax=x;
  }
}

void stats (int a, int b, int c, int d, int *pmin, int *pmax, float *pmoy) {
  if (a<=0){
      *pmin = -1;
      *pmax = -1;
      *pmoy = -1;}
  else if (b<=0){
      *pmoy= a ;
      *pmin= a;
      *pmax= a;
  }else if (c<=0){
    *pmoy= (float)(a+b)/2;
    *pmin= a;
    *pmax= a;
    min_max(b,pmin,pmax);
  }else if (d<=0){
    *pmoy= (float)(a+b+c)/3;
    *pmin= a;
    *pmax= a;
    min_max(b,pmin,pmax);
    min_max(c,pmin,pmax);
  }else {
    *pmoy = (float)(a+b+c+d)/4;
    *pmin= a;
    *pmax= a;
    min_max(b,pmin,pmax);
    min_max(c,pmin,pmax);
    min_max(d,pmin,pmax);
  }
}

void afficher_resultat(float moyenne, int min, int max) {
  printf("max = %d, min = %d, moy = %.2f\n", max, min, moyenne);
}

int main() {
   int min = 3, max = 8;
   int a, b, c, d;
   float moy;

   printf("min = %d, max = %d. Saisissez une valeur entiere :\n", min, max);
   scanf("%d", &a);
   min_max(a,&min,&max);
   printf("La plus grande des 3 valeurs est %d, la plus petite %d.\n", max, min);

   printf("Saisissez trois autres valeurs entieres :\n");
   scanf("%d", &b);
   scanf("%d", &c);
   scanf("%d", &d);

   stats(a,b,c,d,&min,&max,&moy);
   afficher_resultat(moy, min, max);
   return 0;
}
