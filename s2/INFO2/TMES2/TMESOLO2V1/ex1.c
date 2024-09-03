/* Nous souhaitons calculer la somme des valeurs d'un tableau (d'entiers strictement positifs) multiples d'une valeur donnee (M).

- Completez la fonction sommeMultiples pour qu'elle retourne la somme des valeurs du tableau multiples d'une valeur donnee. La fonction doit prendre en parametres le tableau, sa taille et la valeur.

- Completez la fonction main pour afficher le resultat. Le message affiche doit dependre du resultat de l'appel
  a la fonction sommeMultiples. N'oubliez pas de remplacer les ... en parametre des appels a printf.

Les elements du tableau,sa taille et la valeur M a laquelle comparer les elements du tableau 
sont definis par des primitives #define, ces valeurs seront modifiees
pour tester votre programme. Vous pouvez les modifier pour effectuer des tests.
*/

 
#include <stdio.h>

#define M 3
#define VALTAB {3,5,6,8,9,10}
#define TAILLE 6

... sommeMultiples(...) {
/* hypothese : le tableau contient des valeurs strictement positives */

}

int main() {
  /* NE MODIFIEZ PAS L'INSTRUCTION SUIVANTE
  ELLE PERMET D'INITIALISER LE TABLEAU */
  int tab[] = VALTAB;   
  
  /* Affichage */
  printf("La somme des multiples de %d est %d\n",...);
  
  printf("Le tableau ne contient aucun multiple de %d\n",...);
  
  return 0;
}
 
