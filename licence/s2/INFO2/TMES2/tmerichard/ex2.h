/* Dans cet exercice, nous allons manipuler des listes de cartes, chacune d'elle est representee par sa valeur et sa couleur, une liste corrrespont a un jeu de cartes */

typedef struct _carte carte;

/* valeur : valet = 11, dame = 12, roi = 13, as = 1
   couleur : trefle=1, carreau=2, coeur=3, pique=4 */
typedef struct _carte {
  int valeur;
  int couleur;
  carte * suivant;
} carte;

  
/* Ajoute la carte de valeur val et couleur coul EN TETE du jeu passe en parametre.
Retourne la nouvelle tete de liste */
carte *ajouterCarte(carte *mon_jeu, int val, int coul);

/* Affiche les caracteristiques d'un element de la liste */
void afficherCarte(carte *une_carte);
  
/* Affiche toutes les cartes de la liste mon_jeu */
void afficherJeu(carte *mon_jeu);

/* Renvoie le pointeur sur la carte de valeur val et couleur coul presente dans le liste mon_jeu
   la fonction renvoie NULL si la carte n'est pas presente */
carte *trouverCarte(carte *mon_jeu, int val, int coul);
 
/* Joue la carte dont la valeur et la couleur sont passees en parametre, 
  retire de la liste mon_jeu la carte jouee, renvoie la tete de liste
  Attention, si la valeur et la couleur passees en parametre ne correspondent pas a une carte de la 
  liste mon_jeu, cette derniere n'est pas modifiee */
carte *jouerCarte(carte *mon_jeu, int val, int coul);

/* Renvoie la valeur de la paire la plus elevee presente dans la liste mon_jeu.
Renvoie -1 si le jeu ne contient aucune paire */
int trouverPaires(carte *mon_jeu);

/* Cree une liste en recopiant de la liste passee en parametre les cartes de la couleur passee en parametre. Renvoie la tete de la nouvelle liste. La liste initiale n'est pas modifiee. Renvoie null si l aliste initiale ne contient aucune carte de la couleur demander */
carte *listeCouleur(carte *mon_jeu, int coul);
