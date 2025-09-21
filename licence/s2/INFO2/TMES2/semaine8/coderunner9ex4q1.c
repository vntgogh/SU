int Inclus(element_t *e1, element_t *e2) {
  while(e1&&e2){
    if(e1->valeur!=e2->valeur){
      return 0;
    }else{
      if(e1->frequence <= e2->frequence){
        e1=e1->suivant; e2=e2->suivant;
      }else{
          return 0;
      }
    }
  }if(!e1){
      return 1;
  }
  return 0;
}