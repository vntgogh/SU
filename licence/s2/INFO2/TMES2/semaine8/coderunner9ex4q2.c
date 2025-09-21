int Intersection_vide(element_t *e1, element_t *e2) {
  while(e1&&e2){
    if(e1->valeur == e2->valeur){
      return 0;
    } if (e1->valeur < e2->valeur){
      e1=e1->suivant;
    }else{
      e2=e2->suivant;
    }
  }return 1;
}