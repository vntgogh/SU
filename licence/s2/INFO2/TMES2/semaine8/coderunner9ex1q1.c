element_t *Recherche_val(element_t *ensemble, int val) {
  element_t *tmp = malloc(sizeof(element_t));
  if (ensemble==NULL){
      return NULL;
  }
  while (ensemble){
     if (ensemble->valeur == val){
       tmp->valeur = ensemble->valeur;
       tmp->frequence = 2*tmp->valeur;
       return tmp;
     } else {
       ensemble = ensemble->suivant;
     }
  }
  return NULL;
}
