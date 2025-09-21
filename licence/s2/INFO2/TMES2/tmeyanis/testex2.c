#include <stdio.h>
#include "ex2.h"

/* programme de test */ 
int main() {
  produit *liste =NULL;
  liste = ajouterProduitTete(1, 2.50, 5, liste);
  liste = ajouterProduitTete(85, 7.99, 2, liste);
  liste = ajouterProduitTete(468, 15.00, 4, liste);
  liste = ajouterProduitTete(59, 0.99, 26, liste);
  liste = ajouterProduitTete(112, 11.49, 1, liste);
  afficherListe(liste);
  
  printf("\n");
  produit *ch= chercherProduit(468, liste);
  afficherProduit(ch);
  
  printf("\n");
  liste= enleverProduit(112, liste);
  afficherListe(liste);

  printf("\n");
  liste=acheterProduit(85, liste, 3);
  afficherListe(liste);

  printf("\n");
  produit *liste0=NULL;
  liste0 = ajouterProduitTete(5, 2.49, 4, liste0);
  liste0 = ajouterProduitTete(88, 7.99, 3, liste0);
  liste0 = ajouterProduitTete(468, 15.00, 6, liste0);
  liste0 = ajouterProduitTete(77, 0.99, 45, liste0);

  produit *listefusion=NULL;
  listefusion=fusionnerListes(liste, liste0);
  afficherListe(listefusion);
}