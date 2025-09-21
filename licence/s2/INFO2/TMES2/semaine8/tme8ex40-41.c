#include <stdio.h>
#include <stdlib.h>

typedef struct cellule {
    int donnee;
    struct cellule *suivant;
} cellule_t;


cellule_t *creerListe(int taille) { //ex40q1
    cellule_t *tete = NULL;
    int i;
    for (i = 0; i < taille; i++) {
        cellule_t *nouvelleCellule = malloc(sizeof(cellule_t));
        nouvelleCellule->donnee = i;
        nouvelleCellule->suivant = tete;
        tete = nouvelleCellule;
    }
    return tete;
}

void AfficherListeInt(cellule_t *liste) { //ex40q2
    //cellule_t *cel = liste;
    while (liste) {
        printf("%d ", liste->donnee);
        liste = liste->suivant;
    }
    printf("\n");
}

int nboc(cellule_t *l, int val){ //ex41q1
  int nb=0;
  while(l){
    if (l->donnee == val){
      nb++;
    }l=l->suivant;
  }return nb;
}

int plusgrand(cellule_t *l, int val){ //ex41q2
  while(l){
    if(l->donnee < val){
      return 0;
    } l=l->suivant;
  }return 1;
}

cellule_t *max(cellule_t *l){ //ex41q3
  cellule_t *m=l, *tmp=l->suivant;;
  while(tmp ){
    if(tmp->donnee > m->donnee){
      m=tmp;
    }tmp= tmp->suivant;
  } return m;
}

int donneepos(cellule_t *l, int pos){ //ex41q4
  int i=0;
  while(l){
    if(i==pos){
      return l->donnee;
    }l=l->suivant;i++;
  }return l->donnee;
}

cellule_t *Concatener_it(cellule_t *l1, cellule_t *l2){ //ex41q5
  if (!l1 && !l2) 
    return NULL;
  if (!l1 && l2) 
    return l2;
  if (l1 && !l2)
    return l1;
  else{
    cellule_t *tmp=l1;
    while(tmp->suivant){
      tmp=tmp->suivant;
    }tmp->suivant = l2;
  } return l1;
}

int nb_maximum(cellule_t *liste){ //ex41q6
  cellule_t *n=max(liste);
  int cpt=0;
  while(liste){
    if(liste->donnee == n->donnee){
      cpt++;
    }liste= liste->suivant;
  }return cpt;
}

int main() {
    cellule_t *maListe = creerListe(10);
    cellule_t *ml=creerListe(5);
    AfficherListeInt(maListe);
    cellule_t *ma=max(maListe);
    printf("la donnee maximale est %d\n",ma->donnee);
    printf("la donnee en 4e position est %d\n", donneepos(maListe, 4));

    Concatener_it(maListe, ml);
    AfficherListeInt(maListe);
    printf("le maximum apparait %d fois\n",nb_maximum(ml));
    return 0;
}