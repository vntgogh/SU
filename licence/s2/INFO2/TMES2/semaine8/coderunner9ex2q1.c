element_t *Supprime_total_element(element_t * ensemble, int val) {
    /*element_t *tmp;
    element_t *tete = ensemble;
    while(ensemble){
        if (ensemble->valeur == val){
            tmp = ensemble->suivant;
            free(tmp);
            ensemble = tmp;
        }else{
            ensemble = Supprime_total_element(ensemble->suivant,val);
        }
        
    }
    return tete;*/
    
    element_t *tete = ensemble, *precedent = NULL;
    while(ensemble!=NULL && ensemble->valeur!=val){
        precedent = ensemble;
        ensemble = ensemble->suivant;
    } if (ensemble!=NULL){
        if(precedent){
            precedent->suivant=ensemble->suivant;
        }else{
            tete = ensemble->suivant;
        } free(ensemble);
    } return tete;
}

