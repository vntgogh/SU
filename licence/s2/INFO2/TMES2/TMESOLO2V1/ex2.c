#include <stdio.h>
#include <stdlib.h>
#include "ex2.h"

/* Ajoute un nouvel adherent (d'identifiant id) en tete de la liste listeAdherents, le solde et le nombre de vente associes sont initialises a 0
Retourne la nouvelle tete de liste */
adherent *ajouterAdherentTete(int id, adherent *listeAdherents){
 return NULL;
}

/* affiche les caracteristiques d'un adherent */
/* NE PAS MODIFIER LA FONCTION */
void afficherAdherent(adherent *adh) {
  printf("Adherent : %d, solde : %.2f, ventes : %d\n",adh->identifiant,adh->solde,adh->nbVentes);
}

/* Affiche les caracteristiques de tous les adherents de la liste listeAdherents*/
void afficherListe(adherent *listeAdherents){
  
}
  
/* Effectue la vente entre deux adherents, met a jour le solde du vendeur (+ somme) et celui de l'acheteur (-somme) et le nombre de ventes du vendeur */
/* Hypothese : le vendeur et l'acheteur sont dans la liste */
void vente(int vendeur, int acheteur, float somme, adherent *listeAdherents){
  
}

/* Retourne le nombre moyen de ventes par vendeur (nombre de ventes / nombre de vendeurs). Un adherent est considere comme vendeur des qu'il a effectue une vente. Retourne 0.0 si aucun adherent n'a effectue de vente */
float nbMoyenVente(adherent *listeAdherents) {
  return 0.0;
}

/* Fusionne les deux adherents passes en parametre, le premier adherent passe en parametre recupere le solde et le nombre de ventes du second, le second est supprime de la liste. Retourne la tete de liste. 
La fonction doit liberer la memoire */
/* Hypothese : les deux adherents sont dans la liste */
adherent *fusionAdherents(int adh1, int adh2, adherent *listeAdherents) {
  return NULL;
}

/* Cree la liste des adherents non vendeurs (pas de vente), retourne la tete de la liste creee. Dans la noyfvelle liste, le solde de chaque adherent est le meme que dans la liste initiale. Ne modifie pas la liste
passee en parametre */
adherent *listeNonVendeurs(adherent *listeAdherents) {
  return NULL;
}
