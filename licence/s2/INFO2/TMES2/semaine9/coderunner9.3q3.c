element_t *Supprime_element_ensemble_trie(element_t * ensemble, int val) {
    element_t *prec=NULL, *tmp=ensemble;
    
    while(tmp && tmp->valeur < val){
        prec = tmp;
        tmp = tmp->suivant;
    }
    if(!tmp){
       return ensemble;
    }
    if (tmp==ensemble){
        ensemble=ensemble->suivant;
        //return ensemble;
    }else if(tmp->valeur == val){
        if(tmp->frequence==1){
            prec->suivant = tmp->suivant;   
        }else{
           tmp->frequence --; 
        }
    }return ensemble;
}