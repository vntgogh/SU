#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//#define DEBSEED 42
#define NB_VALEURS 1000
#define VMIN 0
#define VMAX 32000

/* Question 1: le programme tire NB_VALEURS aléatoires et en extrait la plus
   grande et la plus petite
*/

int valeur_aleatoire(int min, int max){
  /*
   * retourne un nombre pseudo-aleatoire entre min et max (inclus)
   */
  return min + rand() % (max - min + 1);
}

void minimum_maximum(int val, int* oldmin, int* oldmax){
  /* *oldmin contient en sortie le minimun entre *oldmin en entree et val
   * *oldmax contient en sortie le maximum entre *oldmax en entree et val
   */
  if(val < *oldmin)
    *oldmin = val;
  if(val > *oldmax)
    *oldmax = val;
}

int main(){
  int i, val;
  int min=VMAX, max=VMIN;
  //srand(DEBSEED);
  srand(time(NULL));
  
  for(i=0; i < NB_VALEURS; i++){
    val=valeur_aleatoire(VMIN, VMAX);
    minimum_maximum(val, &min, &max);
  }
  
  printf("MIN = %d, MAX=%d\n", min, max);
  return 0;
}
