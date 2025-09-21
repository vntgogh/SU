#include <stdio.h>

int recherche(int *tab, int taille, int val){ //ex32q1
  for (int i=0; i<taille; i++){
    if(*(tab+i)== val){
      return 1;
    }
  }return 0;
} //ex32q2 les cas d'arret: qd on trouve l'element et qd l'element n'est pas dans le tab

int rechrec(int *tab, int g, int d, int val){ //q3
  if(g>d){return 0;}
  int mid= (g+d)/2;
    if(tab[mid]==val){return 1;}
    else{
      if(val<mid){return rechrec(tab, g, mid-1, val);
        }else{return rechrec(tab, mid+1, d, val);}
    }      
}

int estdeb(char *ch1, char *ch2){ //ex33q1
  if(ch1[0]=='\0' || ch2[0]=='\0'){
    return 1;
  }if(ch1[0] != ch2[0]){
    return 0;
  }else{
    return estdeb(ch1+1, ch2+1);
  }
}

int estinc(char *ch1, char *ch2){ //ex33q2
  if (ch2[0]=='\0'){
    return 0;
  }else{
      if(estdeb(ch1,ch2)==1){
        return 1;
      }else{
        return estinc(ch1,ch2+1);
      }
  }
}

int pasdebinc(char *ch1, char *ch2){ //faux
  if (ch2[0]=='\0'&&ch1[0]=='\0'){
    return 0;
  }else{
      if(estinc(ch1,ch2)==1 && estinc(ch2,ch1)==1){
        return 1;
      }else{
        if (estinc(ch1,ch2)==0){
          return pasdebinc(ch1,ch2+1);
        }else{
          return pasdebinc(ch1+1,ch2);
        }
      }
  }
}

int main() {
    /*int tab[] = {3, 1, 5, 2, 4};
    int n = 5;
    int x = 2;
    int res = recherche(tab, n, x);
    printf("Resultat de la recherche : %d\n", res);*/
  char c1[10]="alphabet";
  char c2[10]="beta";
  printf("%d\n",pasdebinc(c1,c2));
    return 0;
}
