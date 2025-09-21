float calcul_solde(float tab[][NB_JOURS], int id) {
    float solde=0;
    for (int i =0; i< NB_AMIS; i++){
        for (int j =0; j<NB_JOURS;j++){
            if ( i == id ){
                solde += tab[i][j];
            }
        }
    }
    return solde;
}

void affiche_soldes(float tab[][NB_JOURS]) {
  /* format d'affichage a respecter pour chaque membre
  du groupe */
  for ( int i = 0; i <NB_AMIS; i++){
    printf("Solde pour %d : %.2f\n", i, calcul_solde(tab, i));
    }
}
