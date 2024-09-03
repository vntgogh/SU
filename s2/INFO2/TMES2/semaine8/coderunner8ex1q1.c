int nb_occurences(int val, cellule_t *ma_liste) {
  int cpt=0;
  if (ma_liste == NULL){
    return 0;
  }
   while(ma_liste != NULL){
      if(ma_liste->donnee == val){
        cpt++;
      }
      ma_liste=ma_liste->suivant;
   }
   return cpt;
}

int main() {
   int el, n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &el);
   printf("%d\n", nb_occurences(el, ma_liste));
   return 0;
}