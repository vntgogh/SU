#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NBTOURS 10
#define NBLANCERS 2
#define NBQUILLES 10

int lancer(int qdebout) {
  return rand() % qdebout+1;
}

void score(int *score, int *action, int *lancer){
  if(*action>0){
    *score+=2*(*lancer);
    *action-=1;
  }else{
    *score+=*lancer;
  }
}

void tour(int qdebout, int *s, int *a){
      int l=lancer(qdebout);
      printf("lancer 1 -> quilles renversees : %d\n",l);
      if (l==qdebout){ //STRIKE
        *a=2;
        *s+=l;
        printf("GG STRIKE \n");
        int i=0;
        while(*a){
          l=lancer(qdebout);
          printf("lancer extrastrike %d -> quilles renversees :%d\n",i,l);
          score(s,a,&l);
        }
      }else{
        l=l+lancer(qdebout-l);
        printf("lancer 2 -> quilles renversees : %d\n",l);
        if (l==qdebout){ //SPARE
          printf("ET UN SPARE \n");
          *a=1;
          *s+=l;
          while(*a){
            l=lancer(qdebout);
            printf("lancer extraspare -> quilles renversees :%d\n",l);
            score(s,a,&l);
          }
        }else{
          score(s,a,&l);
        }
      }
}

int jeu(int qdebout) {
  int sco=0, act=0;
  for (int i=1;i<=NBTOURS;i++){
    printf("TOUR %d\n",i);
      tour(qdebout, &sco, &act);
    printf("SCORE DE CE TOUR : %d\n",sco);  
  }  
  printf("votre score final est %d\n",sco);
}

int main() {
  int sheesh= 0, spare= 1, strike = 2;
  int scorej=0, score_tot=0;
  srand(time(NULL));
  jeu(NBQUILLES);
  return 0;
}