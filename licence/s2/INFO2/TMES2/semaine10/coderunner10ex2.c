#include <stdlib.h>
#include <stdio.h>

typedef struct _element_t element_t;

struct _element_t{
   int valeur;
   int frequence;
   element_t *suivant;
};


/*element_t* supprime_frequence_inf_seuil(element_t* ens, int seuil) {
    element_t *p=ens,*prec=NULL;
    if (!ens){return NULL;}
    while(p){
        if (p->frequence < seuil){
            if(!prec){
                ens=p->suivant;
                free(p);
                p=ens;
            }else{
                prec->suivant=p->suivant;
                free(p);
                p=prec->suivant;
            }
        }else{
            prec=p;
            p=p->suivant;
        }
    }return ens;
}*/
element_t* supprime_frequence_inf_seuil(element_t *ens, int seuil){
        element_t *pred = NULL, *curr = ens;
        if(!ens) return NULL;
        while(curr){
            if(curr->frequence < seuil){
                if(!pred){
                    ens = curr->suivant;
                    free(curr);
                    curr = ens;
                    
                }
                else{
                    pred->suivant = curr->suivant;
                    free(curr);
                    curr = pred->suivant;
                }
            }
            else{
                pred = curr;
                curr = curr->suivant;
            
            }
            
        }
    return ens;
}

int main() {
   int n, s;
   scanf("%d", &n);
   /* creation d'un multi-ensemble contenant n valeurs differentes */
   element_t* multiE = creer_multiEnsemble(n);
   scanf("%d", &s);
   affiche_ensemble(multiE);
   printf("seuil : %d. ", s);
   multiE = supprime_frequence_inf_seuil(multiE, s);
   affiche_ensemble(multiE);
   return 0;
}