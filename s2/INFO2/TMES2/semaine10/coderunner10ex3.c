#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t{
   int valeur;
   int frequence;
   element_t *suivant;
};

element_t* ajout_suivant(element_t* element, int val, int freq) {
    element_t *nv=malloc(sizeof(element_t));
    nv->valeur= val;
    nv->frequence=freq;
    if(!element){
        return nv;
    }else{
        element_t *tmp=element->suivant;
       element->suivant=nv; 
       nv->suivant=tmp;
    }
    return nv;
}

int main() {
   int val, freq;
   scanf("%d", &val);
   scanf("%d", &freq);
   element_t* prems = ajout_suivant(NULL, val, freq);
   scanf("%d", &val);
   scanf("%d", &freq);
   element_t* deuz = ajout_suivant(prems, val, freq);
   scanf("%d", &val);
   scanf("%d", &freq);
   if (val < deuz-> valeur) {
      ajout_suivant(prems, val, freq);
   }
   else {
      ajout_suivant(deuz, val, freq);
   }
   affiche_ensemble(prems);
   return 0;
}