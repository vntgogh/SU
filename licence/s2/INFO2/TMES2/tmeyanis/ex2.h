/* Dans cet exercice, nous considerons une liste de courses (liste de produits à acheter), chaque element de la liste correspond a un produit et est caracterise par sa reference, son prix et la quantite a acheter */

typedef struct _produit produit;

typedef struct _produit {
  int reference;
  float prix;
  int quantite;
  produit* suivant;
} produit;

/* Ajoute le produit de reference ref, de prix prix et de quantite quant en tete de la liste listeCourses.
Retourne la nouvelle tete de liste */
produit *ajouterProduitTete(int ref, float prix, int quant, produit *listeCourses);

/* Affiche les caracteristiques d'un produit */
void afficherProduit(produit *prod);

/* Affiche les caracteristiques de tous les produits de la liste */
void afficherListe(produit *listeCourses);

/* Retourne le pointeur sur la premiere occurrence du produit dont la reference est passee en parametre 
Retourne NULL si le produit n'est pas dans la liste */
produit *chercherProduit(int ref, produit *listeCourses);

/* Enleve de la liste la premiere occurrence du produit dont la reference est passee en parametre.
Retourne la tete de liste 
La fonction doit liberer la memoire. */
/* Hypothèses : la liste contient un element de reference ref */
produit *enleverProduit(int ref, produit *listeCourses);

/* Met a jour la liste listeCourses apres l'achat du produit dont la reference est passee en parametre. Le produit est achete dans la quantite en parametre. Si cette quantite est superieure ou egale a celle associee au produit dans la liste, ce dernier est supprime de liste. Sinon la quantite de la liste est mise a jour et doit indiquer le nombre d'exemplaires du produit restant. Retourne la tete de liste apres modification. On suppose qu'une meme reference n'est presente qu'une seule fois dans la liste. Attention, le produit peut ne pas etre dans la liste, dans ce cas cette derniere ne doit pas etre modifiee */
produit *acheterProduit(int ref, produit *listeCourses, int quantite);

/* Cree une nouvelle liste qui est la fusion des deux listes passees en parametre.
Dans la nouvelle liste, chaque produit present dans une des deux listes passees en parametre ne doit apparaitre qu'une seule fois (avec la bonne quantite). Retourne la tete de la liste creee */
produit *fusionnerListes(produit *listeCourses1, produit *listeCourses2);