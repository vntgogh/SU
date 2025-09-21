#include <stdio.h>
#include <stdlib.h>

int * fusion (int tab1[], int taille1, int tab2[], int taille2) {
/* realise la fusion triee des tableaux tries tab1 et tab2 */
    int taille3= taille1+taille2;
    int *tab = malloc(sizeof(int)*taille3);
    int i1=0,i2=0,i3=0;
    while (i1!=taille1 && i2!=taille2){
      if (i3<taille3){
        if (tab1[i1]<tab2[i2]){
          tab[i3]= tab1[i1];
          i1++;
          i3++;
        } else {
          tab[i3]= tab2[i2];
          i2++;
          i3++;
        }

      }

    }
    while (i1==taille1 && i2!= taille2){
            tab[i3]= tab2[i2];
            i3++;
            i2++;
      }
    while (i2==taille2 && i1!= taille1) {
            tab[i3]= tab1[i1];
            i3++;
            i1++;
    }
    return tab;
}

int main() {
    int tab1[20];
    int tab2[20];
    int i;
    int nb1;
    int nb2;
    int *tab;

    scanf("%d", &nb1);
    scanf("%d", &nb2);
    for(i = 0; i < nb1; i++) {
        scanf("%d", tab1 + i);
    }
    for(i = 0; i < nb2; i++) {
        scanf("%d", tab2 + i);
    }

    tab = fusion(tab1, nb1, tab2, nb2);
    for (i = 0; i < nb1 + nb2; i++) {
        printf("%d  ", tab[i]);
    }
    printf("\n");
    free(tab);
    return 0;
}
