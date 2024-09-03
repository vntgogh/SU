#include <stdio.h>
#include "multi_ensembles.h"


int main() {
   element_t *ensemble = NULL;
  
  // Ajout de quelques éléments
  ensemble = Ajout_tete_ensemble(ensemble, 42, 1);
  ensemble = Ajout_tete_ensemble(ensemble, 24, 3);
  ensemble = Ajout_tete_ensemble(ensemble, 15, 2);
  Affiche_ensemble(ensemble);
  printf("\n");
  supprimetot(ensemble,42);
  supprimeel(ensemble,24);
  Affiche_ensemble(ensemble);
  ensemble = supptrie(ensemble, 15);
  Affiche_ensemble(ensemble);
    element_t *e1= NULL, *e2=NULL; //ex46
  e1 = Ajout_tete_ensemble(ensemble, 15, 1);
  e1 = Ajout_tete_ensemble(ensemble, 24, 3);
  e1 = Ajout_tete_ensemble(ensemble, 42, 2);

  e2 = Ajout_tete_ensemble(ensemble, 11, 3;
  e2 = Ajout_tete_ensemble(ensemble, 24, 1);
  e2 = Ajout_tete_ensemble(ensemble, 42, 2);
  e2 = Ajout_tete_ensemble(ensemble, 45, 2);
    printf("0 = e1 non inclus dans e2, 1= e1 inclus dans e2 -> %d\n", inclus(e1,e2));
    printf("0 = intersection non vie, 1 = intersection vide -> %d\n", inter(e1,e2));
  
}