#include <stdio.h>
#include <stdlib.h>
typedef struct _note note;

typedef struct _note{
  int note;
  int effectif;
  note* suivant;
} note;

note * ajouterNoteTete(int une_note, int effectif, note *listeNotes){
  note *nv= malloc(sizeof(note));
  nv->note=une_note;
  nv->effectif= effectif;
  nv->suivant=listeNotes;
  listeNotes=nv;
  return listeNotes;
}

void afficherNote(note *p){
  printf("Note : %d\n", p->note);
  printf("Effectif : %d\n", p->effectif);
}

void afficherListe(note *listeNotes){
  while(listeNotes){
    afficherNote(listeNotes);
    listeNotes=listeNotes->suivant;
  }
}

int validerListe(note *listeNotes){
  while(listeNotes){
    if(listeNotes->effectif>0 && 0>listeNotes->note && listeNotes->note >100){
      return 0;
    }listeNotes=listeNotes->suivant;
  }return 1;
}

note *supprimerzero(note *listeNotes){
  note *prec=NULL, *p=listeNotes;
  while(p){
    if(p->effectif==0){
        note*tmp=p;
        p=p->suivant;
        free(tmp);
        if(!prec){
          listeNotes=p;
        }else{ prec->suivant=p;}
    }else{
      prec=p;
      p=p->suivant;
    }
  }
  if(listeNotes && listeNotes->effectif==0){
    listeNotes=listeNotes->suivant;
  }
  return listeNotes;
}

note *notePresente(int une_note, note *listeNotes){
  note *p=NULL;
  while(listeNotes){
    if(listeNotes->note== une_note){
      p=listeNotes;
      return p;
    }listeNotes=listeNotes->suivant;
  }return NULL;
}

note *fusionListes(note *liste1, note *liste2){
  while(liste2){
      note *p=notePresente(liste2->note, liste1);
        if(p){
          p->effectif+=liste2->effectif;
        }else{
        liste1=ajouterNoteTete(liste2->note, liste2->effectif, liste1); 
        }
    liste2=liste2->suivant;
  }
  return liste1;
}

int main(){
  note *l=NULL;
  l=ajouterNoteTete(4, 0, l);
  l=ajouterNoteTete(3, 2, l);
  l=ajouterNoteTete(10, 4, l);
  
  //afficherNote(l);
  //afficherListe(l);
  printf("%d\n", validerListe(l));
  l=supprimerzero(l);
  //afficherListe(l);
  note *pr=NULL;
  pr=notePresente(10, l);
  //afficherNote(pr);

  note *l2=NULL;
  l2=ajouterNoteTete(6, 3, l2);
  l2=ajouterNoteTete(3, 8, l2);
  l=fusionListes(l, l2);
  afficherListe(l);
}