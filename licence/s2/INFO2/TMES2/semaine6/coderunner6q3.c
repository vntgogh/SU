int recherche_rec_aux (int tab[], int taille, int i, int val) {
    if (i==taille){
            int ind= -1;
            return ind;
    } else {
        if (tab[i] == val){
          int ind= i;
          return ind;
        }else{
          return recherche_rec_aux(tab,taille, i+1, val);
       }
    }
}

int recherche_rec(int tab[], int taille, int elem) {
    return recherche_rec_aux (tab, taille, 0, elem);
}
