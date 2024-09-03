#include <stdio.h>
#include <stdlib.h>

typedef struct _adherent adherent;

typedef struct _adherent {
  int identifiant;
  float solde;
  int nbVentes;
  adherent* suivant;
} adherent;

/* Ajoute un nouvel adherent (d'identifiant id) en tete de la liste listeAdherents, le solde et le nombre de vente associes sont initialises a 0
Retourne la nouvelle tete de liste */
adherent *ajouterAdherentTete(int id, adherent *listeAdherents){
  adherent *tete,*nv=malloc(sizeof(adherent));
  nv->solde=0;
  nv->identifiant = id;
  nv->nbVentes =0;
  nv->suivant = listeAdherents;
  tete=nv;
 return tete;
}

/* affiche les caracteristiques d'un adherent */
/* NE PAS MODIFIER LA FONCTION */
void afficherAdherent(adherent *adh) {
  printf("Adherent : %d, solde : %.2f, ventes : %d\n",adh->identifiant,adh->solde,adh->nbVentes);
}

/* Affiche les caracteristiques de tous les adherents de la liste listeAdherents*/
void afficherListe(adherent *listeAdherents){
  while(listeAdherents){
    afficherAdherent(listeAdherents);
    listeAdherents=listeAdherents->suivant;
  }  return NULL;
}
  
/* Effectue la vente entre deux adherents, met a jour le solde du vendeur (+ somme) et celui de l'acheteur (-somme) et le nombre de ventes du vendeur */
/* Hypothese : le vendeur et l'acheteur sont dans la liste */
afherent vente(int vendeur, int acheteur, float somme, adherent *listeAdherents){
  adherent *p1=listeAdherents, *p2=listeAdherents;
  while(p1 && p1->identifiant != vendeur){
    p1=p1->suivant;
  }if(p1){
    p1->solde += somme;
    p1->nbVentes++;
  }while(p2 && p2->identifiant != acheteur){
    p2=p2->suivant;
  }if(p2){
    p2->solde -= somme;
  }return listeAdherents; 
}

/* Retourne le nombre moyen de ventes par vendeur (nombre de ventes / nombre de vendeurs). Un adherent est considere comme vendeur des qu'il a effectue une vente. Retourne 0.0 si aucun adherent n'a effectue de vente */
float nbMoyenVente(adherent *listeAdherents) {
  adherent *p=listeAdherents; int nbvend=0, nbvent=0; 
  while(p){
    if(p->nbVentes > 0){
      nbvent+=p->nbVentes;
      nbvend++;
    } p=p->suivant;
  }if(nbvend != 0){
    return nbvent / nbvend;
  }return 0.0;
}

/* Fusionne les deux adherents passes en parametre, le premier adherent passe en parametre recupere le solde et le nombre de ventes du second, le second est supprime de la liste. Retourne la tete de liste. 
La fonction doit liberer la memoire */
/* Hypothese : les deux adherents sont dans la liste */
adherent *fusionAdherents(int adh1, int adh2, adherent *listeAdherents) {
  adherent *p=listeAdherents, *prec=NULL;
  while(p){
    if(p->identifiant == adh1){
      if(!prec){
        listeAdherents = p->suivant;
        free(p);
        p=listeAdherents;
      }
    }if(p->identifiant == adh2){
      adherent *nv=malloc(sizeof(adherent));
      if(p->identifiant == adh1){
        nv=ajouterAdherentTete(p->identifiant,nv);
        p= p->suivant;
      }if {
        nv->nbVentes += p->nbVentes;
        nv->solde+=p->solde;
        prec->suivant = p->suivant;
        free(p);
        p=prec->suivant;
      }
    }prec=p;p=p->suivant;
  }
  return listeAdherents;
}

/* Cree la liste des adherents non vendeurs (pas de vente), retourne la tete de la liste creee. Dans la noyfvelle liste, le solde de chaque adherent est le meme que dans la liste initiale. Ne modifie pas la liste
passee en parametre */
adherent *listeNonVendeurs(adherent *listeAdherents) {
  adherent *nvl=NULL;
  while(listeAdherents){
    if(listeAdherents->nbVentes ==0){
      nvl = ajouterAdherentTete(listeAdherents->identifiant, nvl);
    }
  } return nvl;
}

int main(){
  adherent *l=NULL;
  l=ajouterAdherentTete(05, l);
  l=ajouterAdherentTete(04, l);
  l=ajouterAdherentTete(03, l);
  l=ajouterAdherentTete(02, l);
  l=ajouterAdherentTete(01, l);
  l=ajouterAdherentTete(00, l);
  vente(02, 00, 2.5, l);
  vente(02, 01, 2.5, l);
  vente(00, 03, 10.99, l);
  vente(01, 03, 48.5, l);
  vente(00, 03, 0.51, l);
  printf("nb vente moyen:%.2f\n",nbMoyenVente(l));
  fusionAdherents(01, 03, l);
  adherent *n=NULL;
  //n=listeNonVendeurs(l);
  afficherListe(l);
  afficherListe(n);
}