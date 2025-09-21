#include <stdio.h>
#define MAX 100

int premier(int n){
  if(n < 2)
    return 0;
  for(int i=2; i <= n/2; i++)
    if((n % i) == 0)
      return 0;
  return 1;
}

void affiche(int n_max){
  for(int i=2; i <= n_max; i++)
    if(premier(i)==0)
      printf("%d ", i);
  printf("\n");
}

int main(){
  affiche(MAX);
  return 0;
}
