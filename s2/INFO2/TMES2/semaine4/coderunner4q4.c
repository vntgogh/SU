int insertElt(int tab[], int el, int *nbEl, int taille){
    int ind = indiceInsert(tab,el,*nbEl,taille);
    if (ind == -1){
        return 0;
    } else {
      int tmp;
      for(int i=ind;i<taille-1;i++){
        tmp = tab[i];
        tab[i]=el;
        el = tmp;
      }
    }
    *nbEl= *nbEl+1;
    return 1;
}

void affiche_tab(int tab[], int taille) {
    int i;
    for (i = 0; i < taille; i++) {
        printf("%d  ", tab[i]);
    }
    printf("\n");
}

int main() {
   int tab[6];
   int i, inser_OK, nbEl, val;

   scanf("%d", &nbEl);
   for (i = 0; i < nbEl; i++) {
      scanf("%d", tab + i);
   }
   scanf("%d", &val);

   inser_OK = insertElt(tab, val, &nbEl, 6);
   printf("insertion OK ? %d\n", inser_OK);
   affiche_tab(tab, nbEl);
   return 0;
}
