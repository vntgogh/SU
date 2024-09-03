#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "ex2.h"


typedef struct _carte carte;

/* valeur : valet = 11, dame = 12, roi = 13, as = 1
   couleur : trefle=1, carreau=2, coeur=3, pique=4 */
typedef struct _carte {
  int valeur;
  int couleur;
  carte * suivant;
} carte;


/* Ajoute la carte de valeur val et couleur coul EN TETE du jeu passe en parametre.
Renvoie la nouvelle tete de liste */
carte *ajouterCarte(carte  *mon_jeu, int val, int coul) {
  carte *nv =malloc(sizeof(carte));
  nv->valeur=val;
  nv->couleur=coul;
  nv->suivant= mon_jeu;
  return nv;
}

/* Affiche les caracteristiques d'un element de la liste */
/* NE PAS MODIFIER LA FONCTION */
void afficherCarte(carte *une_carte) {
  if (une_carte->valeur > 1 && une_carte->valeur <= 10) {
    printf("%d de ",une_carte->valeur);
  } else {
    switch(une_carte->valeur) {
      case 1 : printf("As de "); break;
      case 11 : printf("Valet de "); break;
      case 12 : printf("Dame de "); break;
      case 13 : printf("Roi de ");
    }
  }
  
  switch(une_carte->couleur) {
    case 1 : printf("trefle\n"); break;
    case 2 : printf("carreau\n"); break;
    case 3 : printf("coeur\n"); break;
    case 4 : printf("pique\n");
  }
}
  
/* Affiche toutes les cartes de la liste mon_jeu */
void afficherJeu(carte *mon_jeu){
  while(mon_jeu){
    afficherCarte(mon_jeu);
    mon_jeu=mon_jeu->suivant;
  }  
}

/* Renvoie le pointeur sur la carte de valeur val et couleur coul presente dans le liste mon_jeu la fonction renvoie NULL si la carte n'est pas presente */
carte *trouverCarte(carte *mon_jeu, int val, int coul){
  carte *p=NULL;
  while(mon_jeu){
    if(mon_jeu->valeur == val){
      if(mon_jeu->couleur == coul){
        p=ajouterCarte(p,mon_jeu->valeur,mon_jeu->couleur);
        return p;
      }
    } mon_jeu=mon_jeu->suivant;
  }return NULL;
}

/* Joue la carte dont la valeur et la couleur sont passees en parametre, 
  retire de la liste mon_jeu la carte jouee, renvoie la tete de liste
  Attention, si la valeur et la couleur passees en parametre ne correspondent pas a une carte de la 
  liste mon_jeu, cette derniere n'est pas modifiee */
carte *jouerCarte(carte *mon_jeu, int val, int coul){
  carte *prec=NULL, *p=mon_jeu;
  while(p && (p->valeur!=val||p->couleur != coul)){
    prec=p;
    p= p->suivant;
  }if(prec){
    if(p){
      carte *tmp=p->suivant;
      free(p);
      prec->suivant=tmp;
    }
  }else{
    carte *tmp=p->suivant;
    free(p);
    return tmp;
  }return mon_jeu;
}

/* Renvoie la valeur de la paire la plus elevee presente dans la liste mon_jeu 
Renvoie -1 si le jeu ne contient aucune paire */
int trouverPaires(carte *mon_jeu){
  carte *p1=mon_jeu->suivant;
  int max=-1;
  if(mon_jeu == NULL){ // Cas où le jeu est vide
    return max;
  }
  while(p1 && mon_jeu){
    if(mon_jeu->valeur==p1->valeur){
      if(p1->valeur > max){
        max=p1->valeur;
      }
    } mon_jeu=mon_jeu->suivant;p1=p1->suivant;
  }
  return max;
}

/*int trouverPaires(carte *mon_jeu) {
  carte *i = mon_jeu, *j = mon_jeu;
  int max = -1;
  //On crée une boucle imbriqué pour chercher les paires, et on stocke leurs max dans une variable
  while(i){
    while(j){
      //On écrit i différent de j, pour ne pas qu'on compare les 2 mêmes éléments, autrement dit, 2 éléments qui ont la même adresse
      // si la valeur de i est égale à la valeur de j, alors c'est une paire
      if(i != j && i->valeur == j->valeur && i->valeur > max){
        max = i->valeur;
      }
      j= j->suivant;
    }
    i = i->suivant;
    j = mon_jeu;
  }
  return max;
}*/

/* Cree une liste en recopiant de la liste passee en parametre les cartes de la couleur passee en parametre. Renvoie la tete de la nouvelle liste. La liste initiale n'est pas modifiee. Renvoie null si l aliste initiale ne contient aucune carte de la couleur demander */
carte *listeCouleur(carte *mon_jeu, int coul) {
  carte *nvl= NULL;
  while(mon_jeu){
    if(mon_jeu->couleur == coul){
      nvl=ajouterCarte(nvl,mon_jeu->valeur,coul);
    } mon_jeu=mon_jeu->suivant;
  } if (!nvl) {
    return NULL;
  }
  return nvl;
}
