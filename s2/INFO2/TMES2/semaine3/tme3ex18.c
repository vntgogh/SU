#include <stdio.h>
#include <stdlib.h>

void echange(int a, int b){
  int tmp=a;
  a=b;
  b=tmp;
  printf("%d,%d\n",a, b);
}

void tri(int *a, int *b){
  if(*a>*b){
    int tmp=*a;
    *a=*b;
    *b=tmp;
  }
}

void tri3(int *a, int *b, int *c){
  if (*a<*b && *a<*c && *b>*c){
    tri(b,c);
  }if (*a>*b && *a>*c && *b>*c){
    tri(a,c);
  }if (*a>*b && *a<*c && *b<*c){
    tri(a,b);
  } 
}

int main(){
  int a=2, b=1, c=3;
  tri3(&a,&b,&c);
  printf("%d,%d,%d\n",a,b,c);
}