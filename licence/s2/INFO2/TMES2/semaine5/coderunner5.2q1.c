void init_zero(float tab[][NB_JOURS], int taille) {
    int i=0, j=0;
    for (i =0 ; i < taille; i++){
        for (j=0; j< NB_JOURS; j++){
          tab[i][j]= 0;
      }
    }
}
