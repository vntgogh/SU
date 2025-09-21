#include <stdio.h>
#include "ex2.h"

/* programme de test */ 
int main() {
 
 char *ch= "jejz";
 caractere *ml=NULL;
 ml=frequenceCaracteres(ch);
 afficherListe(ml);
  caractere *p=NULL;
  p=chercherCaractere('e',ml);
  printf("%c a la frequence la + elevee\n",maxFrequence(ml) );
  printf("%c\n", p->caract);
  caractere *mll=NULL;
  mll=ajouterCaractereTete('c',2,mll);
  mll=ajouterCaractereTete('b',1,mll);
  mll=ajouterCaractereTete('a',0,mll);
  mll=supprimeZero(mll);
  afficherListe(mll);
  return 0;
  
}
  