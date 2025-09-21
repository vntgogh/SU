element_t *Supprime_total_element_ensemble_trie(element_t * ensemble, int val) {
    element_t *tmp, *prec;
    tmp = prec = ensemble;

    while (tmp != NULL && tmp->valeur != val) {
        prec = tmp;
        tmp = tmp->suivant;
    }
        if (tmp == ensemble) {  
            ensemble = ensemble->suivant;   
        } if (!tmp){
            return ensemble;
        } else {
            prec->suivant = tmp->suivant; 
        }
    
    return ensemble;
}