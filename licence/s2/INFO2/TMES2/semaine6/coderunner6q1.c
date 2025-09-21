int recherche_iter(int tab[], int taille, int val) {
 int i=0;
 while ( tab[i] != val ){
   if (i == taille-1){
     return -1;
   } else{
    i++ ;
   }
 }
 if (tab[i] == val){
        return i;
 } else {
       return -1;
 }

}
