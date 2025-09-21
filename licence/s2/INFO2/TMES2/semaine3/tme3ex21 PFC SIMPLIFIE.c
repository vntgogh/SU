#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define PIERRE 1
#define FEUILLE PIERRE+1
#define CISEAUX FEUILLE+1
#define NBESSAIS 3
#define POINTSGAGNANTS 3

int choix_ordinateur(void) {
  return rand() % (3);
}

int choix_joueur() {
  int i;
  int n =scanf("%d",&i);
  if(n<1 && n>3){
    for (int j=0;j<NBESSAIS; j++){
      printf("valeur incorrecte, veuillez ressayer");
      n=scanf("%d",&i);
    }
  }return n;
}

void score(int cj, int co,int *sj, int *so){
  if (cj==PIERRE+co || co==FEUILLE+cj){
    *so=*so+1;
    printf("l'ordi a marque\n");
  }else if (co==PIERRE+cj || cj==FEUILLE+co){
    *sj=*sj+1;
    printf("vous avez marque\n");
  }else{
    printf("pas de point\n");
  }
}

void jeu() {
  int score_j=0, score_o=0;
  while (score_j<POINTSGAGNANTS && score_o< POINTSGAGNANTS){
    int cj = choix_joueur();
    int co = choix_ordinateur();
    score(cj,co,&score_j, &score_o);
  }
  if(score_o== POINTSGAGNANTS){
    printf("HAHA SALE BOUFFON T NUL\n");
  }if(score_j== POINTSGAGNANTS){
    printf("GG BOUFFON\n");
  }
}

int main() {
  srand(time(NULL));
  jeu();
  return 0;
}