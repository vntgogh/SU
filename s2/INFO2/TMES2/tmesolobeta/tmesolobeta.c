#include <stdio.h>
#define VALTAB {1,4,8}
#define TAILLE 3

float moyennePos(int taille, int *tab){
  float moy=0.0; int count=0;
  for(int i=0; i<taille; i++){
    if( *(tab+i) > 0){
      moy+= *(tab+i);
      count++;
    }
  }if(count ==0) return -1;
  return (moy/count);
}

int main(){
  int tab[]= VALTAB;
  float m= moyennePos(TAILLE, tab);
  printf("%.2f\n", m);
}