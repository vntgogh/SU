element_t * Ajout_tete_ensemble(element_t *ensemble, int val, int freq) {
  element_t *res=Recherche_val(ensemble, val);
  element_t *tete = malloc(sizeof(element_t));
  if (res == NULL){
    tete->valeur = val;
    tete->frequence = freq;
    tete->suivant=ensemble;
  }else{
    element_t *tmp2 = ensemble;
    tete= tmp2;
    while(tmp2){
        if (tmp2->valeur == val){
            tmp2->frequence = tmp2->frequence + freq;
        }
        tmp2=tmp2->suivant;
    }
  }
  return tete;
}
