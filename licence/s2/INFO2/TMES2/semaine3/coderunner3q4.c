#include <stdio.h>
#include <math.h>

int discriminant(int x, int y , int z) {
    int disc= y * y - 4* x * z;
    return disc;
}

int nb_racines_delta(int x, int y , int z) {
    int d= discriminant(x,y,z);
    int nb_racines=0;
    if (d==0){
        nb_racines =1;
    }
    if (d>0){
        nb_racines = 2;
    }
    else if (d<0) {
        nb_racines=0;
    }
    return  nb_racines;
}

int racines(float *x1, float *x2, int x, int y, int z) {
    int d= discriminant(x,y,z);
    int n= nb_racines_delta(x,y,z);

    if (n==2){
        *x1= ((-y+0.0) + sqrt(d))/(2*x);
        *x2= ((-y+0.0) - sqrt(d))/(2*x);
        return 2;
    } else if (n==1){
        *x1= ((-y+0.0)/(2*x));
        return 1;
    } else {
        return 0;
    }
}

int main(){
   int a,b,c;
   int nb_rac;
   float rac1, rac2;

   printf("Entrez les coefficients a (!= 0) b et c du polynome :\n");
   scanf("%d", &a);
   scanf("%d", &b);
   scanf("%d", &c);

   printf("valeur de delta : %d\n", discriminant(a,b,c));
   nb_rac = racines(&rac1,&rac2, a,b,c);
   if (nb_rac == 2){
      printf("Le polynome a 2 racines : %.3f et %.3f\n", rac1, rac2);
   }
   if (nb_rac == 1){
      printf("Le polynome a 1 racine double : %.3f\n", rac1);
   }
   if (nb_rac == 0){
      printf("Le polynome n'a pas de racine reelle.\n");
   }
   return 0;
}
