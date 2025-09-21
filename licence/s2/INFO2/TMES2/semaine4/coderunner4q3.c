int indiceInsert(int tab[], int el, int nb, int taille){
    int ind =0;
    int k=0;
    if (taille <= nb){
      ind = -1;
    }else{
        for (k=0; k<nb; k++){
            if (el == tab[k]){
                return -1;
            }if (el > tab[nb-1]){
                ind = nb;
            }if (el < tab[k]){
                return k;
            }
        }
    }
  return ind;
}
