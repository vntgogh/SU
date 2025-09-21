#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NBAMIS 3
#define NBJOURS 5

int nbmots(char *ch){ //ex27
  int cpt=0, i=0;
  while (*(ch+i) != '\0'){
    if(*(ch+i+1)== ' ' && *(ch+i)!= ' '){
      cpt++;
    }
    i++;
  }
  return cpt;
}

void init_tab(float tab[][NBJOURS]){ //q1ex28
  for (int i=0; i<NBAMIS;i++){
    for (int j=0;j<NBJOURS;j++){
      tab[i][j]=0;
    }
  }
}

void comptj(float tab[][NBJOURS], int jour){ //q2ex28
  int ami= rand() % NBAMIS;
  int montant= (rand()%21)+30;
  for (int i=0;i<NBAMIS;i++){
    if (i==ami){
      tab[i][jour]+=NBAMIS*(montant/NBAMIS);
    }else{
      tab[i][jour] += -montant/NBAMIS;
    }
  }printf("Jour %d: %d paye %.2f\n",jour,ami,tab[ami][jour]);
}

float msolde(float tab[][NBJOURS],int ami){
  float solde=0;
  for (int o=0;o<NBJOURS;o++){
    solde+=tab[ami][o];
  }
  return solde;
}

void affichetab(float tab[][NBJOURS]){  
  for (int k=0; k<NBAMIS;k++){
    for (int m=0;m<NBJOURS;m++){
      printf("t[%d][%d] = %.2f\n",k,m,tab[k][m]);
    }
  }
}

int main() {  
  char c[25]= "jsuis ines ";
  float t[NBAMIS][NBJOURS];
  srand(time(NULL));
  init_tab(t);
  for (int j = 0; j < NBJOURS; j++) {
    comptj(t, j);
  }
  for(int s=0; s<NBAMIS;s++){
    printf("Solde de l'ami %d : %.2f\n", s,msolde(t,s));
  }
  //affichetab(t);
  //printf("%d\n", nbmots(c));
  
}
  