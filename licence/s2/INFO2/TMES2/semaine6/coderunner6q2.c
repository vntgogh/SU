int recherche_rec(int tab[], int taille, int val) {

 int i=taille-1;
     if (tab[i] == val){
        int ind= i;
        return ind;
     } else {
        if (i<0){
            int ind= -1;
            return ind;
        }else{
            return recherche_rec(tab, i, val);
       }
     }

}

