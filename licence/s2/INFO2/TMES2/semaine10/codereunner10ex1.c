#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t{
   int valeur;
   int frequence;
   element_t *suivant;
};

int taille(element_t* ens) { 
    int cpt=0;
    if(!ens){
        return 0;
    }else{
        cpt+= ens->frequence;
        return taille(ens->suivant)+cpt;
    }
}

int main() {
   int n;
   scanf("%d", &n);
   /* creation d'un multi-ensemble contenant n valeurs differentes */
   element_t* multiE = creer_multiEnsemble(n);
   printf("%d\n", taille(multiE));
   return 0;
}