#include <stdio.h>
#include <stdlib.h>
#include "ex2.h"

//gcc -o ex2 ex2.c testex2.c 

typedef struct _produit produit;

typedef struct _produit {
  int reference;
  float prix;
  int quantite;
  produit* suivant;
} produit;


/* Ajoute le produit de reference ref, de prix prix et de quantite quant en tete de le liste listeCourses.
Retourne la nouvelle tete de liste */
produit *ajouterProduitTete(int ref, float prix, int quant, produit *listeCourses) {
  produit *nv= malloc(sizeof(produit));
  nv->reference=ref;
  nv->prix=prix;
  nv->quantite=quant;
  nv->suivant=listeCourses;
  return nv;
}

/* Affiche les caracteristiques d'un produit */
/* NE PAS MODIFIER CETTE FONCTION */
void afficherProduit(produit *prod){
  printf("Ref=%d,prix:%.2f, quant:%d\n",prod->reference,prod->prix,prod->quantite); 
}

/* Affiche les caracteristiques de tous les produits de la liste */
void afficherListe(produit* listeCourses){
    while(listeCourses){
        afficherProduit(listeCourses);
        listeCourses=listeCourses->suivant;
    }
}

/* Retourne le pointeur sur la premiere occurrence du produit dont la reference est passee en parametre 
Retourne NULL si le produit n'est pas dans la liste */
produit *chercherProduit(int ref, produit *listeCourses) {
  produit *p=malloc(sizeof(produit));
  while(listeCourses){
    if(listeCourses->reference == ref){
        p=ajouterProduitTete(listeCourses->reference,listeCourses->prix,listeCourses->quantite,p);
        return p;
    } listeCourses=listeCourses->suivant;
  }return NULL;
}


/* Enleve de la liste la premiere occurrence du produit dont la reference est passee en parametre.
Retourne la tete de liste.
La fonction doit liberer la memoire. */
/* Hypothèses : la liste contient un element de reference ref */
produit *enleverProduit(int ref, produit *listeCourses) {
  produit *prec=NULL, *p=listeCourses;
  if(!listeCourses){
    return NULL;
  }
  while(p && p->reference != ref){
    prec=p;
    p=p->suivant;
  }
  if(p){ //la reference est dans la liste
    produit *tmp=p->suivant;
    free(p);
    if(prec){ //la reference n'est pas le premier produit de la liste
        prec->suivant = tmp;
    }else{ //la reference est pas le premier produit de la liste
        prec=tmp;
    }
  }return prec;
}

/* Met a jour la liste listeCourses apres l'achat du produit dont la reference est passee en parametre. Le produit est achete dans la quantite en parametre. Si cette quantite est superieure ou egame a celle associee au produit dans le liste, ce dernier est supprime de liste. Sinon la quantite de la liste est mise a jour et doit indiquer le nombre d'exemplaires du produit restant a acheter. Retourne la tete de liste. Attention, le produit peut ne pas etre dans la liste, dans ce cas cette derniere ne doit pas etre modifiee */
produit *acheterProduit(int ref, produit *listeCourses, int quantite) {
  produit *p=listeCourses;
  while(p){
    if(p->reference == ref){
        if(p->quantite <= quantite){
            p=enleverProduit(ref,listeCourses);
        }else{
            p->quantite = p->quantite - quantite;
        }
    }p=p->suivant;
  } return listeCourses;
}

/* Cree une nouvelle liste qui est la fusion des deux listes passees en parametre.
Dans la nouvelle liste, chaque produit present dans une des deux listes passees en parametre ne doit apparaitre qu'une seule fois (avec la bonne quantite). Retourne la tete de la liste creee */
produit *fusionnerListes(produit *listeCourses1, produit *listeCourses2) {
  produit *nl=NULL;
  if(!listeCourses1 && listeCourses2){ // l1 vide 
    nl=listeCourses2;
    return nl;
  }else if(!listeCourses2 && listeCourses1){ //l2 vide
    nl=listeCourses1;
    return nl;
  }else if(!listeCourses1&& !listeCourses2){ // l1 et l2 vides
    return NULL;
  }

  while(listeCourses1&&listeCourses2){
    produit *p1=chercherProduit(listeCourses1->reference, listeCourses2); //cherche la ref de l1 dans l2
    produit *p2=chercherProduit(listeCourses2->reference, listeCourses1); //cherche la ref de l2 dans l1
    if(p1){ // la ref de l1 est dans l2
        nl= ajouterProduitTete(listeCourses1->reference, listeCourses1->prix, listeCourses1->quantite+p1->quantite,nl);
    }else if(!p1){ // la ref de l1 n'est pas dans l2
        nl= ajouterProduitTete(listeCourses1->reference, listeCourses1->prix, listeCourses1->quantite,nl); 
    }
    if(!p2){ // la ref de l2 n'est pas dans l1 ; on n'ajoute pas les produits quand p2 n'est pas vide car ce sont les doublons des cas ou ^p1 n'est pas vide.
        nl= ajouterProduitTete(listeCourses2->reference, listeCourses2->prix, listeCourses2->quantite,nl);
    }listeCourses1=listeCourses1->suivant;
    listeCourses2=listeCourses2->suivant;
  }
  
  if(!listeCourses2 && listeCourses1){ // l2 entierement ajoutee a nl
    while(listeCourses1){
        nl= ajouterProduitTete(listeCourses1->reference, listeCourses1->prix, listeCourses1->quantite, nl);
      listeCourses1=listeCourses1->suivant;
    }
  }if(!listeCourses1 && listeCourses2){ // l1 entierement ajoutee a nl
    while(listeCourses2){
        nl= ajouterProduitTete(listeCourses2->reference, listeCourses2->prix, listeCourses2->quantite, nl);
      listeCourses2=listeCourses2->suivant;
    }
  }return nl;
}

