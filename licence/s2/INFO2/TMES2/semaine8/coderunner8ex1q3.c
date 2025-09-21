cellule_t* maximum(cellule_t *liste){
  cellule_t* max;
  max= liste;
  if (max == NULL){
    return NULL;
  }
  while(liste != NULL){
    if(liste->donnee > max->donnee){
      max->donnee = liste->donnee;
      liste = liste->suivant;
    }
    liste = liste->suivant;
  }
  return max;
}

int main() {
   int n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   /* la fonction le_max calcule le resultat attendu */
   assert( maximum(ma_liste) == le_max(ma_liste) );
   return 0;
}