/*typedef struct _element_t element_t;
struct _element_t{
  int valeur;
  int frequence;
  element_t *suivant;
};

element_t * Ajout_tete_ensemble(element_t *ensemble, int val, int freq) {
  element_t *ptr=malloc(sizeof(element_t));
    ptr->valeur=val;
    ptr->frequence=freq;
    ptr->suivant=ensemble;
    return ptr;
}

void Affiche_ensemble(element_t *ensemble) {
  element_t *ptr = ensemble;
  
  while (ptr) {
    printf("val : %d, frequence : %d\n",ptr->valeur,ptr->frequence);
    ptr=ptr->suivant;
  }
}*/

element_t *Supprime_element(element_t *ensemble, int val) {

    element_t *tete = ensemble, *precedent = NULL;
    while(ensemble!=NULL && ensemble->valeur!=val){
        precedent = ensemble;
        ensemble = ensemble->suivant;
    }
    if (ensemble){ // si l'ensemble n'est pas vide alors ensemble s'est arrete a l'element de la val 
        if(precedent){ //si precedent est non NULL, il contient tous les premiers elements jusque val exclu
            if(ensemble->frequence==1){ //si freq=1 on supp l'element
                ensemble=ensemble->suivant;
                precedent->suivant=ensemble;
            }else{
                ensemble->frequence --;
            }
        }else{ //si precedent est vide alors la valeur à supp est le 1er element donc on commence au 2e element
            precedent=ensemble->suivant;
            tete = precedent;
        }
    }
    return tete;
}

/*int main() {
      
  element_t * ensemble;
  int val;
  for (val=1; val <=10; val++){
      ensemble=Ajout_tete_ensemble(ensemble,val,val);
  }
  for (val=1; val <=2; val++){
      ensemble=Supprime_element(ensemble,1);
  }
  Affiche_ensemble(ensemble);
  return 0;
}*/