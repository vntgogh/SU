#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MIN 2
#define MAX 5

void lettre(char *ch){ //q1ex29
  int i=0;
  while (*(ch+i)!='\0'){
    if(isalpha(*(ch+i))){
     printf("%c", ch[i]);
    }
    i++;}
}

char* filtre(char *ch){ //q2ex29
  int l= strlen(ch);
  char* res= malloc((l+1) * sizeof(char));
    int ind = 0,i=0;
    while(*(ch+i)!='\0'){
        if (isalpha(ch[i])) {
            res[ind] = ch[i];
            ind++;
        }i++;
    }
    return res;
} //q3ex29 oui mais cela peut poser des problèmes si la chaîne doit être conservée dans son état initial donc il est préférable d'utiliser la 2e fonction

int init_tab(int *tab){ //q1ex30
  int n = (rand()%(MAX-MIN+1))+MIN;
  for (int i=0;i<n;i++){
    tab[i]= rand()%2;
  }tab[n-1]=-1;
  return n;
}

void affiche(int *tab){
  int i=0;
  while (tab[i] != -1){
    printf("%d ",tab[i]);
    i++;
  }
}

int compress_tab(int tab_brut[], int tab_compress[]){ //q2ex30
  /*renvoie le nombre d'elements de tab_compress*/
  int i=0,j=0;
  while(tab_brut[i]!=-1){
    int cpt=0;
    while(tab_brut[i]==tab_brut[i+1]){
      cpt++;
      i++;
    }i++;
    tab_compress[j]=cpt;
    j++;
    tab_compress[j]=tab_brut[i];
    j++;
  }tab_compress[j]=-1;
  return j-1;
}

int decompress_tab(int tab_brut[],int tab_compress[]){ //q3ex30
  int i=0,j=0;
  while(tab_compress[i]!=-1){
    if(tab_compress[i]!=0 &&tab_compress[i]!=1){
      for (int k=0;k<tab_compress[i];k++){
        tab_brut[j]=tab_compress[i+1];
        j++;
      }i=i+2;
    }else{
      tab_brut[j]=tab_compress[i];
      i++;
      j++; 
    }   
  }tab_brut[j]=-1;
  return j;
}

int compare(int *t1,int *t2){
  int i=0, j=0;
  while(t1[i]!=-1 && t2[j]!=-1){
    if(t1[i]!=t2[j]){
      return 0;
    }else{
      i++;
      j++;
    }
  }if (t1[i]!=-1 && t2[j]==-1){
    return 0;
  } if (t1[i]==-1 && t2[j]!=-1){
    return 0;
  }else{
    return 1;
  }
}

int main() {  
  //ex28
  char ch[25]="vnt/gogh/  yo0o";
  lettre(ch);
  char *res = filtre(ch);
  printf("%s\n",res);
  free(res);
  //ex29
  int t[MAX];
  int size =init_tab(t);
  affiche(t);
  //ex30
  int tab_brut[]={0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,-1};
  int tab_comp[18];
  compress_tab(tab_brut,tab_comp);
  printf("%d\n",compress_tab(tab_brut,tab_comp));
  affiche(tab_comp);
  printf("\n");
  int tab_brut2[25];
  int tab_comp2[]={2,0,4,1,0,3,1,2,0,1,4,0,-1};  
  decompress_tab(tab_brut2,tab_comp2);
  printf("%d\n", decompress_tab(tab_brut2,tab_comp2));
  affiche(tab_brut2);
  //ex31
  int tab1[]={1,1,5,4,7,-1};
  int tab2[]={1,1,5,4,7,-1};
  printf("%d\n",compare(tab1,tab2));
}
  