#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "ecosys.h"

/* PARTIE 1*/
/* Fourni: Part 1, exercice 4, question 2 */
Animal *creer_animal(int x, int y, float energie) {
  Animal *na = (Animal *)malloc(sizeof(Animal));
  assert(na);
  na->x = x;
  na->y = y;
  na->energie = energie;
  //valeurs de dir comprises entre -1 inclus et 1 inclus
  na->dir[0] = rand() % 3 - 1;
  na->dir[1] = rand() % 3 - 1;
  na->suivant = NULL;
  return na;
}


/* Fourni: Part 1, exercice 4, question 3 */
Animal *ajouter_en_tete_animal(Animal *liste, Animal *animal) {
  assert(animal);
  assert(!animal->suivant);  //on s'assure que suivant est vide
  animal->suivant = liste;
  return animal;
}

/* A faire. Part 1, exercice 6, question 2 */
void ajouter_animal(int x, int y,  float energie, Animal **liste_animal) {

  assert(x>=0); assert(y>=0); assert(x<SIZE_X); assert(y<SIZE_Y);

  Animal *nva = creer_animal(x, y, energie);//création 
  Animal *ajt = ajouter_en_tete_animal(*liste_animal, nva); // ajout
}

/* A Faire. Part 1, exercice 5, question 5 */
void enlever_animal(Animal **liste, Animal *animal) {
    if (*liste){ 
      if (animal){
        if (*liste == animal) { //si animal est premier element de la liste
          *liste = (*liste)->suivant;
          free(animal);
        }
        Animal *prec = *liste;
        while (prec->suivant){ 
          if (prec->suivant != animal) {
            prec = prec->suivant;
          }
        }if (prec->suivant == animal) { //si animal est present dans la liste
            prec->suivant = animal->suivant;
            free(animal);
          }
      }
    }
}

/* A Faire. Part 1, exercice 6, question 7 */
Animal* liberer_liste_animaux(Animal *liste) {
    Animal *ptr = liste;
    Animal *tmp;
    while (ptr != NULL) {
        tmp = ptr->suivant;
        free(ptr);
        ptr = tmp;
    } return NULL;
}

/* Fourni: part 1, exercice 4, question 4 */
unsigned int compte_animal_rec(Animal *la) {
  if (!la) return 0;
  return 1 + compte_animal_rec(la->suivant);
}

/* Fourni: part 1, exercice 4, question 4 */
unsigned int compte_animal_it(Animal *la) {
  int cpt=0;
  while (la) {
    cpt++;
    la=la->suivant;
  }
  return cpt;
}



/* Part 1. Exercice 5, question 1, ATTENTION, ce code est susceptible de contenir des erreurs... */
void afficher_ecosys(Animal *liste_proie, Animal *liste_predateur) {
  unsigned int i, j;
  char ecosys[SIZE_X][SIZE_Y];
  Animal *pa=NULL, *pe=NULL;

  /* on initialise le tableau */
  for (i = 0; i < SIZE_Y; ++i) {
    for (j = 0; j < SIZE_X; ++j) {
      ecosys[i][j]=' ';
    }
  }

  printf("MARCHE");


  assert(pa); assert(pe);
  /* on ajoute les proies */
  pa = liste_proie;
  while (pa) {
    ecosys[pa->x][pa->y] = '*';
    pa=pa->suivant;
  }

  /* on ajoute les predateurs */
  pe = liste_predateur;
  while (pe) {
      if ((ecosys[pe->x][pe->y] == '@') || (ecosys[pa->x][pa->y] == '*')) { /* proies aussi present */
        ecosys[pe->x][pe->y] = '@';
      } else {
        ecosys[pe->x][pe->y] = 'O';
      }
    pe = pe->suivant;
  }

  /* on affiche le tableau */
  printf("+");
  for (j = 0; j < SIZE_X; ++j) {
    printf("-");
  }  
  printf("+\n");
  for (i = 0; i < SIZE_Y; ++i) {
    printf("|");
    for (j = 0; j < SIZE_X; ++j) {
      putchar(ecosys[i][j]);
    }
    printf("|\n");
  }
  printf("+");
  for (j = 0; j<SIZE_X; ++j) {
    printf("-");
  }
  printf("+\n");
  int nbproie=compte_animal_it(liste_proie);
  int nbpred=compte_animal_it(liste_predateur);
  
  printf("Nb proies : %d\tNb predateurs : %d\n", nbproie, nbpred);

}


void clear_screen() {
  printf("\x1b[2J\x1b[1;1H");  /* code ANSI X3.4 pour effacer l'ecran */
}

/* PARTIE 2*/

/* Part 2. Exercice 4, question 1 */
void bouger_animaux(Animal *la) {
    /*A Completer*/

}

/* Part 2. Exercice 4, question 3 */
void reproduce(Animal **liste_animal, float p_reproduce) {
   /*A Completer*/

}


/* Part 2. Exercice 6, question 1 */
void rafraichir_proies(Animal **liste_proie, int monde[SIZE_X][SIZE_Y]) {
    /*A Completer*/

}

/* Part 2. Exercice 7, question 1 */
Animal *animal_en_XY(Animal *l, int x, int y) {
    /*A Completer*/

  return NULL;
} 

/* Part 2. Exercice 7, question 2 */
void rafraichir_predateurs(Animal **liste_predateur, Animal **liste_proie) {
   /*A Completer*/

}

/* Part 2. Exercice 5, question 2 */
void rafraichir_monde(int monde[SIZE_X][SIZE_Y]){

   /*A Completer*/


}

