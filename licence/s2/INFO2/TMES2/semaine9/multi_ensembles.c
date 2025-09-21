#include <stdio.h>
#include <stdlib.h>
#include "multi_ensembles.h"

  
/* Retourne un pointeur sur le premier element de valeur val, retourne NULL si aucun �l�ment n'a la valeur val */
element_t * Recherche_val(element_t *ensemble, int val) { //ex43q1
  element_t *p=NULL;
    while(ensemble){
      if(ensemble->valeur == val){
        p=ensemble;
        return p;
      }
      ensemble=ensemble->suivant;
    }
  return NULL;
}

/* Ajoute l'element val en tete de l'ensemble s'il n'apparait pas dans l'ensemble, augmente sa frequence de 1 sinon */
element_t * Ajout_tete_ensemble(element_t *ensemble, int val, int freq) { //ex43q2
  element_t *tmp = ensemble, *nv = malloc(sizeof(element_t));
    // Parcours de l'ensemble
  while(tmp){
    // Si l'element existe deja dans l'ensemble, on incremente sa frequence
    if(tmp->valeur == val){
      tmp->frequence += freq;
      return ensemble;
    }
    tmp = tmp->suivant;
  } 
  
  // Si l'element n'existe pas dans l'ensemble, on cree un nouvel element et on l'ajoute au debut de l'ensemble
  if(nv){
    nv->valeur = val;
    nv->frequence = freq;
    nv->suivant = ensemble;
    ensemble = nv;
    return ensemble;
  }
  
  // Si la creation du nouvel element a echoue, on retourne NULL
  return NULL;
}

/* Affche tous les elements d'un ensemble avec leur frequence */
void Affiche_ensemble(element_t *ensemble) {
  element_t *ptr = ensemble;
  
  while (ptr != NULL) {
    printf("val : %d, frequence : %d\n",ptr->valeur,ptr->frequence);
    ptr=ptr->suivant;
  }
}

/* Saisie des n elements d'un ensemble */
element_t * Creation_ensemble(int n) {
  element_t *ensemble=NULL;
  
  int i = 0;
  int val;
  
  for (i=0; i < n; i++) {
    printf("Saisie d'un entier: ");
    scanf("%d",&val);
    ensemble=Ajout_tete_ensemble(ensemble,val,1);
  }
  return ensemble;
}

element_t *supprimetot(element_t *ensemble, int val){ //ex44q1
  element_t *prec=ensemble, *p=NULL;
  while(ensemble && ensemble->valeur != val){
    prec=ensemble;
    ensemble=ensemble->suivant;
  }if (ensemble){
    p=ensemble->suivant;
    free(ensemble);
    prec->suivant = p;
    return prec;
  }return ensemble;
}

element_t *supprimeel(element_t *ensemble, int val){ //ex44q2
  element_t *prec=ensemble, *p=NULL;
  while(ensemble && ensemble->valeur != val){
    prec=ensemble;
    ensemble=ensemble->suivant;
  }if (ensemble){
    if(ensemble->frequence ==1){
      p=ensemble->suivant;
      free(ensemble);
      prec->suivant = p;
      return prec;
    }else{
      ensemble->frequence--;
    }
  }return ensemble;
}

element_t *ajouttrie(element_t *ensemble,int val, int freq){ //ex45q1
  element_t *prec =NULL, *p=ensemble, *nv=malloc(sizeof(element_t));
  while(p && p->valeur<val){
    prec=p;
    p=p->suivant;
  }if(p&&p->valeur==val){
    p->frequence+=freq;
    return p;
  }else{ //p est NULL et val n'est pas dans l'ensemble 
      nv->valeur=val;
      nv->frequence=freq;
      
    if(prec){ //p n'est pas entierement parcouru donc nv se trouve avant les elements restants de p et apres tous les elements precedents 
      prec->suivant = nv;
      nv->suivant=p;
    }else{ //il n'ya pas d'element precedent donc nv doit etre le 1er element de l'ensemble
      nv->suivant=ensemble;
      ensemble=nv;
    }
  }return ensemble;
}

element_t *supptrietot(element_t *ensemble, int val){ //ex45q2
  element_t *prec=NULL, *p=ensemble;
  while(p&&p->valeur<val){ //(*)
    prec=p; 
    p=p->suivant;
  }while(p&&p->valeur==val){ //supprime tous les elements qui ont la valeur val
    element_t *tmp=p; p=p->suivant;free(tmp);
    if(!prec){ //cad que val est le 1er element de ensemble
      ensemble=p; // p pointe deja sur l'element suivant
    }else{
      prec->suivant = p; //prec ne pointe pas encore sur l'element val et p pointe deja sur l'element suivant(*)
    }
  }return ensemble;
}

element_t *supptrie(element_t *ensemble, int val){ //ex45q2
  element_t *p=ensemble,*prec=NULL;
  while(p&&p->valeur <val){
    prec=p;
    p=p->suivant;
  }if(p&&p->valeur==val){ //l'element est present
      if(p->frequence>1){
        p->frequence--;
      }else{ //sa frequence est de 1 donc on supprime entierement l'element
        element_t *tmp=p;
        p=p->suivant;
        free(tmp);
        if(prec){ //si p est le premier element
          prec->suivant = p;
        }else{ //p est le premier et/ou le seul element de l'ensemble
          ensemble=p;
        }
      }
  }return ensemble; 
}

int inclus(element_t *e1, element_t *e2){ //ex46q1
  if(!e1){
    return 1;
  }
  while(e1&&e2){
    if(e1->valeur!=e2->valeur){
      return 0;
    }else{
      if(e1->frequence <= e2->frequence){
        e1=e1->suivant; e2=e2->suivant;
      }else{return 0;}
    }
  }if(!e1){return 1;}
  return 0;
}

int inter(element_t *e1, element_t *e2){ //ex46q2 les deux ensembles sont TRIES
  while(e1&&e2){
    if(e1->valeur == e2->valeur){
      return 0;
    } if (e1->valeur < e2->valeur){
      e1=e1->suivant;
    }else{
      e2=e2->suivant;
    }
  }return 1;
}