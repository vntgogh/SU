#include <stdio.h>
#include <stdlib.h>
#include "ex2.h"

/* Ajoute un nouveau caractere en tete de la liste listeCaracteres, le caractere et sa frequence sont passes en parametre.
Retourne la nouvelle tete de liste */
caractere* ajouterCaractereTete(char c, int freq, caractere* listeCaracteres){
  caractere *nv=malloc(sizeof(caractere));
  nv->caract= c;
  nv->frequence=freq;
  nv->suivant = listeCaracteres;
  listeCaracteres=nv;
 return listeCaracteres;
}

/* affiche les caracteristiques d'un caractere */
/* NE PAS MODIFIER LA FONCTION */
void afficherCaractere(caractere *c){
  printf("caractere : %c, frequence : %d\n",c->caract,c->frequence);
}

/* Affiche les caracteristiques de tous les elements de la liste listeCaracteres */
void afficherListe(caractere* listeCaracteres) {
 while (listeCaracteres){
  afficherCaractere(listeCaracteres);
  listeCaracteres=listeCaracteres->suivant;
 }
}

/* Retourne le caractere qui a la frequence la plus elevee, si plusieurs caracteres sont concernes, retourne le dernier de la liste. Retourne le caractere '0' si la liste est vide */
char maxFrequence(caractere *listeCaracteres) {
  caractere *m=malloc(sizeof(caractere));
  if(!listeCaracteres){
    return '0';
  }
  m=listeCaracteres;
  listeCaracteres=listeCaracteres->suivant;
  while(listeCaracteres){
    if(listeCaracteres->frequence > m->frequence){
      caractere *tmp=m;
      m=listeCaracteres;
      free(tmp);
    }listeCaracteres=listeCaracteres->suivant;
  } return m->caract;  
}

/* Retourne le pointeur sur la premiere apparition du caractere passe en parametre dans la liste listeCaracteres.
Retourne NULL si le caractere n'est pas dans la liste */
caractere* chercherCaractere(char c, caractere* listeCaracteres) {
  caractere *p=malloc(sizeof(caractere));
  while(listeCaracteres){
    if(listeCaracteres->caract == c){
      p=listeCaracteres;
      return p;
    }listeCaracteres=listeCaracteres->suivant;
  }if(!p){return NULL;}
  return p;
}
  
/* Cree et retourne la liste associee a la chaine de caracteres passee en parametre. Chaque element de la liste doit correspondre a un caractere de la chaine et a sa frequence d'apparition dans la chaine. Chaque caractere de la chaine ne doit apparaitre qu'une fois dans la liste */
caractere* frequenceCaracteres(char * chaine) {
  int i=0, j=0;
  caractere *li=NULL;
  while(chaine[i]!= '\0'){
    i++;
  }
  while(chaine[j]!= '\0'){
    caractere *tmp=li;
    li=ajouterCaractereTete(chaine[j],0,li);
    for(int k=0;k<i;k++){
      if(chaine[k]==chaine[j]){
        li->frequence++;
      }
    } j++;
    li->suivant=tmp;
  }
  return li;
}

/* Supprime de la liste listeCaracteres tous les caracteres dont la frequence est egale a zero. Retourne la tete de liste.
La fonction doit liberer la memoire.
Si la chaine passee en parametre est vide, le fonction doit retourner NULL */
caractere *supprimeZero(caractere *listeCaracteres){
  caractere *prec=NULL, *p=listeCaracteres;
  if(!listeCaracteres)
    return NULL;  
  while(p){
    if(p->frequence!=0){
      prec=p;
    }else{
      caractere *tmp=p;
      if (!prec) {
        listeCaracteres = p->suivant;free(tmp);
        return listeCaracteres;
      }else{
        prec->suivant=p->suivant;
      }      
    }
    p=p->suivant;
  }return listeCaracteres;
}