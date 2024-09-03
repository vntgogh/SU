/* Nous souhaitons calculer le nombre d'elements d'un tableau d'entiers superieurs strictement a une valeur donnee (SEUIL).

- Completez la fonction nbSup pour qu'elle retourne le nombre d'elements du tableau superieurs a une valeur donnee. La fonction doit prendre en parametres le tableau, sa taille et la valeur.

- Completez la fonction main pour afficher le resultat. Le message affiche doit dependre du resultat de l'appel
  a la fonction nbSup. N'oubliez pas de remplacer les ... en parametre des appels a printf.

Les elements du tableau, sa taille et la valeur (SEUIL) sont definis par des primitives #define, ces valeurs seront modifiees pour tester votre programme. Vous pouvez les modifier pour effectuer des tests.
*/

#include <stdio.h>

#define VALTAB {1,4,7,8,2}
#define TAILLE_TAB 5
#define SEUIL 5

int nbSup(int *tab, int taille, int val) {
  int cpt=0;
  for(int i=0; i<taille; i++){
    if(*(tab+i) > val){
      cpt++;
    }
  } return cpt;
}

int main() {
  /* NE MODIFIEZ PAS L'INSTRUCTION SUIVANTE
  ELLE PERMET D'INITIALISER LE TABLEAU */
  int tab[] = VALTAB;
 
  /* affichage du resultat */
  printf("Nombre d'elements superieurs strictement a %d : %d\n", nbSup(tab, TAILLE_TAB,SEUIL));
  
  printf("Aucun element superieur strictement a %d\n",SEUIL);!
  return 0;
}
