int tous_plus_grands(int val, cellule_t* ma_liste) {
    if (ma_liste == NULL){
    return 1;
    }
    while(ma_liste != NULL){
      if(ma_liste->donnee < val){
        return 0;
      }
      ma_liste=ma_liste->suivant;
    }
    return 1;
}

int main() {
   int el, n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &el);
   printf("%d\n", tous_plus_grands(el, ma_liste));
   return 0;
}