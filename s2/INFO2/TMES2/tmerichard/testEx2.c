#include <stdio.h>
#include "ex2.h"

/* programme de test */
int main() {
  carte *n= NULL;
  n=ajouterCarte(n,4,2);
  n=ajouterCarte(n,10,3);
  n=ajouterCarte(n,4,1);
  n=ajouterCarte(n,10,1);
  n=ajouterCarte(n,10,2);
  //afficherJeu(n);
  carte *tr=NULL;
  tr=trouverCarte(n,10,2);
  //afficherJeu(tr);
  n=jouerCarte(n, 4, 2);
  //afficherJeu(n);
  int m=trouverPaires(n);
  //printf("%d\n", m);
  
  carte *nli=NULL;
  nli=listeCouleur(n,1);
  afficherJeu(nli);
}