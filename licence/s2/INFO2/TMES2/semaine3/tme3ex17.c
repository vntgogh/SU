#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_VALEURS 50
#define VMIN -20
#define VMAX 20

int neg=0,pos=0,zero=0;

int valeur_aleatoire(int min, int max)
{
  return min+ rand() % (max-min +1);
}

void pos_neg(int n){
    if(n<0){
      neg++;
    }if(n==0){
      zero++;
    }else{
      pos++;
    }
}

int main(){
  /* initialisation du g�n�rateur de nombres al�atoires */
  srand(time(NULL));
  
  for(int i=0; i<NB_VALEURS; i++){
    int n = valeur_aleatoire(VMIN,VMAX);
    printf("%d\n",n);
    pos_neg(n);
  }printf("%d valeurs positives, %d valeurs négatives, %d zeros\n", pos, neg , zero);
  return 0;
}