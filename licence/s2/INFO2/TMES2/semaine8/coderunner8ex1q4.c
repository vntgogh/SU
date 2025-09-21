int renvoyer_val_element_pos(int pos, cellule_t* liste){
   int i =0;
   while (i != pos){
       i++ ;
       liste =liste->suivant;
   }
   return liste->donnee;
}

int main() {
   int i, n;
   scanf("%d", &n);
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &i);
   assert (i >= 0 && i < n);
   printf("%d\n", renvoyer_val_element_pos(i, ma_liste));
   return 0;
}