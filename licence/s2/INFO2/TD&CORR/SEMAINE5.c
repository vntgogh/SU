#include <stdio.h>
#include <stdlib.h>

char *int_to_str(int n){
  int cpt=0;
  int tmp =n ;
  while (tmp){
    tmp = tmp/10;
    cpt++;
  }
  char *ch = malloc(cpt*sizeof(char));
  int tmp2;
  for(int i=cpt-1;i>=0;i--){
    tmp2 = n %10;
    ch[i] = tmp2+48;
    n=n/10;
  }
  return ch; 
}

int indice_min(int tab[], int taille){
  int min= tab[0];
  int i;
  for( i =0; i<taille; i++){
    if (min > *(tab+i)){
      min = *(tab+i);
    }
  }
  return i;  
}


int main() {
  int t[5]={5,9,8,2,3};
  printf("%d",indice_min(t,5));
  printf("%d", int_to_str(1048));
  return 0;
}
  