element_t * Ajout_ensemble_trie(element_t *ensemble, int val, int freq) {

    element_t *tmp, *prec, *nv;
    tmp = prec = ensemble;

    while (tmp != NULL && tmp->valeur < val) {
        prec = tmp;
        tmp = tmp->suivant;
    }
    if (tmp != NULL && tmp->valeur == val) { //la valeur est deja dans le multi ensemble
        tmp->frequence += freq;
    } else { //p->valeur > val donc il faut inserer nv
        nv = malloc(sizeof(element_t));
        nv->valeur = val;
        nv->frequence = freq;
        nv->suivant = tmp; //tmp equivaut a tous les elements de l'ensemble superieurs à val

        if (tmp == ensemble) { //cad que l'on est pas entré dans le while et que tmp->valeur > val 
            ensemble = nv;     //et que tmp n'a pas ete modifié donc ensemble est vide
        } else {
            prec->suivant = nv;// sinon prec qui comprend tous les elements inferieurs à val sont suivis de nv  
        }                       //lui meme suivi de tmp(comprend tous les elements superieurs a val)
    }
    return ensemble;
}