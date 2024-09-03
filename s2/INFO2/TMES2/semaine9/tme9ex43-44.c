#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;
struct _element_t{
  int valeur;
  int frequence;
  element_t *suivant;
};
element_t * Recherche_val(element_t *ensemble, int val) { //ex43q1
  element_t *p=NULL;
    while(ensemble){
      if(ensemble->valeur == val){
        p=ensemble;
        return p;
      }
      ensemble=ensemble->suivant;
    }
  return NULL;
}

/* Ajoute l'element val en tete de l'ensemble s'il n'apparait pas dans l'ensemble, augmente sa frequence de 1 sinon */
element_t * Ajout_tete_ensemble(element_t *ensemble, int val, int freq) { //ex43q2
  element_t *tmp = ensemble, *nv = malloc(sizeof(element_t));
  
  // Parcours de l'ensemble
  while(tmp){
    // Si l'element existe deja dans l'ensemble, on incremente sa frequence
    if(tmp->valeur == val){
      tmp->frequence += freq;
      return ensemble;
    }
    tmp = tmp->suivant;
  }
  
  // Si l'element n'existe pas dans l'ensemble, on cree un nouvel element et on l'ajoute au debut de l'ensemble
  if(nv){
    nv->valeur = val;
    nv->frequence = freq;
    nv->suivant = ensemble;
    ensemble = nv;
    return ensemble;
  }
  
  // Si la creation du nouvel element a echoue, on retourne NULL
  return NULL;
}

/* Affche tous les elements d'un ensemble avec leur frequence */
void Affiche_ensemble(element_t *ensemble) {
  element_t *ptr = ensemble;
  
  while (ptr != NULL) {
    printf("val : %d, frequence : %d\n",ptr->valeur,ptr->frequence);
    ptr=ptr->suivant;
  }
}

/* Saisie des n elements d'un ensemble */
element_t * Creation_ensemble(int n) {
  element_t *ensemble=NULL;
  
  int i = 0;
  int val;
  
  for (i=0; i < n; i++) {
    printf("Saisie d'un entier: ");
    scanf("%d",&val);
    ensemble=Ajout_tete_ensemble(ensemble,val,1);
  }
  return ensemble;
}

int main() {
   element_t *ensemble = NULL;
  
  // Ajout de quelques éléments
  ensemble = Ajout_tete_ensemble(ensemble, 42, 1);
  ensemble = Ajout_tete_ensemble(ensemble, 24, 3);
  Affiche_ensemble(ensemble);
}
  