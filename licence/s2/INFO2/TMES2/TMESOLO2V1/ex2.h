/* Dans cet exercice, nous considerons un site de ventes entre les membres inscrits. Nous nous interessons plus particulierement a la liste des adherents. Chaque adherent est represente par un identifiant (un entier), le solde de ses transactions et le nombre de ventes qu'il a realisees */

typedef struct _adherent adherent;

typedef struct _adherent {
  int identifiant;
  float solde;
  int nbVentes;
  adherent* suivant;
} adherent;

/* Ajoute un nouvel adherent (d'identifiant id) en tete de la liste listeAdherents, le solde et le nombre de vente associes sont initialises a 0
Retourne la nouvelle tete de liste */
adherent *ajouterAdherentTete(int id, adherent *listeAdherents);

/* Affiche les caracteristiques d'un adherent */
void afficherAdherent(adherent *adh);

/* Affiche les caracteristiques de tous les adherents de la liste listeAdherents*/
void afficherListe(adherent *listeAdherents);

/* Effectue la vente entre deux adherents, met a jour le solde du vendeur (+ somme) et celui de l'acheteur (-somme) et le nombre de ventes du vendeur */
/* Hypothese : le vendeur et l'acheteur sont dans la liste */
void vente(int vendeur, int acheteur, float somme, adherent *listeAdherents);

/* Retourne le nombre moyen de ventes par vendeur (nombre de ventes / nombre de vendeurs). Un adherent est considere comme vendeur des qu'il a effectue une vente. Retourne 0.0 si aucun adherent n'a effectue de vente */
float nbMoyenVente(adherent *listeAdherents);
  
/* Fusionne les deux adherents passes en parametre, le premier adherent passe en parametre recupere le solde et le nombre de ventes du second, le second est supprime de la liste. Retourne la tete de liste. 
La fonction doit liberer la memoire */
/* Hypothese : les deux adherents sont dans la liste */
adherent *fusionAdherents(int adh1, int adh2, adherent *listeAdherents);

/* Cree la liste des adherents non vendeurs (pas de vente), retourne la tete de la liste creee. Dans la noyfvelle liste, le solde de chaque adherent est le meme que dans la liste initiale. Ne modifie pas la liste
passee en parametre */
adherent *listeNonVendeurs(adherent *listeAdherents);