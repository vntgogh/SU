#include <stdio.h>

typedef struct _planete {

   float densite;
   float distance;
   int nbsat;
   char nom[10];
} planete;


void affichePlanete(planete p){
   printf("%s : densite = %.2f, distance soleil = %.1f, nb satellites = %d\n",p.nom, p.densite, p.distance, p.nbsat);
}

int main(){
   planete p;

   scanf("%s", p.nom);
   scanf("%f", &p.densite);
   scanf("%f", &p.distance);
   scanf("%d", &p.nbsat);
   affichePlanete(p);
   return 0;
}
