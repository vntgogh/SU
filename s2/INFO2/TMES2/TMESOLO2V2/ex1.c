/* Nous souhaitons compter le nombre de cases identiques de deux tableaux d'entiers de meme taille.
   Deux cases sont identiques si elles sont au meme indice et contiennnent la meme valeur.
 
- Completez la fonction nbCaseId pour qu'elle retourne le nombre de cases identiques de deux tableaux.
  La fonction doit prendre en parametres les deux tableaux et leur taille commune.

- Completez la fonction main pour afficher le resultat. Le message affiche doit dependre du resultat de l'appel
  a la fonction nbCaseId. N'oubliez pas de remplacer les ... en parametre des appels a printf.

Les elements des tableaux et leur taille sont definis par des primitives #define, 
ces valeurs seront modifiees pour tester votre programme.
Vous pouvez les modifier pour effectuer des tests.
*/
  

#include <stdio.h>

#define TAILLE 4
#define VALTAB1 {1,4,7,2}
#define VALTAB2 {1,3,7,4}

int nbCaseId(int *t1, int *t2, int taille) {
  int cpt=0;
  for(int i=0; i<taille; i++){
    if(t1[i] == t2[i]){
      cpt++;
    }
  }return cpt;
}

int main() {
  /* NE MODIFIEZ PAS LES INSTRUCTIONS SUIVANTES
  ELLES PERMETTENT D'INITIALISER LES TABLEAUX */
  int tab1[TAILLE] = VALTAB1;
  int tab2[TAILLE] = VALTAB2;

  printf("Les tableaux contiennent %d case(s) identique(s)\n", nbCaseId(tab1,tab2));
 
  printf("Les tableaux ne contiennent aucune case identique\n");
  
  return 0;
}

