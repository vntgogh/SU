#include <stdio.h>
#include <time.h>
#define TMIN -200
#define TMAX 300

void init_temp(float tab[], int len){
  for (int i =0 ; i <len ; i++){
    tab[i]= rand() % (TMAX-TMIN)+TMIN;
  }
}

void affiche(float tab[], int len){
    for (int i =0 ; i <len ; i++){
      printf("tab[%d] = %1.f\n", i, tab[i]);
    }
}

float moy_temp(float tab[], int len){
  int s=0;
  for (int i=0; i<len; i++){
    s+= tab[i];
  }
  return s/len;
}

int tneg(float tab[], int len){
  int cpt=0;
  for (int i =0; i<len; i++){
    if (tab[i]<0){
      cpt++;
    }
  }
  if (cpt==0){
    printf("Aucune temperature au-dessous de zero.\n");
  }
  return cpt;
}

int main() {
    float tabf[31];
    srand(time(NULL));
    init_temp(tabf, 31);
    affiche(tabf, 31);
    printf("la temp moyenne est %2.f\n", moy_temp(tabf, 31));
    tneg(tabf, 31);
    printf("il y a %d jours a temp negative\n", tneg(tabf, 31));
    return 0;
}
  