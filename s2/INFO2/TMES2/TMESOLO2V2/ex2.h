/* Dans cet exercice, nous considerons une liste permettant de stocker des caractères et leur fréquence */

typedef struct _caractere caractere;

typedef struct _caractere{
  char caract;
  int frequence;
  caractere * suivant;
} caractere;

/* Ajoute un nouveau caractere en tete de la liste listeCaracteres, le caractere et sa frequence sont passes en parametre.
Retourne la nouvelle tete de liste */
caractere *ajouterCaractereTete(char c, int freq, caractere *listeCaracteres);

/* affiche les caracteristiques d'un caractere */
/* NE PAS MODIFIER LA FONCTION */
void afficherCaractere(caractere *c);

/* Affiche les caracteristiques de tous les elements de la liste listeCaracteres */
void afficherListe(caractere *listeCaracteres);

/* Retourne le caractere qui a la frequence la plus elevee, si plusieurs caracteres sont concernes, retourne le dernier de la liste. Retourne le caractere '0' si la liste est vide */
char maxFrequence(caractere *listeCaracteres);

/* Retourne le pointeur sur la premiere apparition du caractere passe en parametre dans la liste listeCaracteres.
Retourne NULL si le caractere n'est pas dans la liste */
caractere *chercherCaractere(char c, caractere *listeCaracteres);
  
/* Cree et retourne la liste associee a la chaine de caracteres passee en parametre. Chaque element de la liste doit correspondre a un caractere de la chaine et a sa frequence d'apparition dans la chaine. Chaque caractere de la chaine ne doit apparaitre qu'une fois dans la liste */
caractere *frequenceCaracteres(char * chaine);

/* Supprime de la liste listeCaracteres tous les caracteres dont la frequence est egale a zero. Retourne la tete de liste.
La fonction doit liberer la memoire.
Si la chaine passee en parametre est vide, le fonction doit retourner NULL */
caractere *supprimeZero(caractere *listeCaracteres);
