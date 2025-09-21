void affecte_depenses(float tab[][NB_JOURS], int jour, float montant, int id) {
    for (int i =0; i< NB_AMIS; i++){
        for (int j =0; j<NB_JOURS;j++){
          tab[id][jour]=(montant/NB_AMIS)*(NB_AMIS-1);
          if ( i != id && j == jour){
            tab[i][j]= -(montant/NB_AMIS);
          }
        }
    }
}
