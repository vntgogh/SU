#include <stdio.h>
#include <math.h>


int discriminant(int a, int b, int c){
    return b*b - 4*a*c; 
}


void afficheRacines(int a, int b, int c) {
    if (discriminant(a,b,c) <0){
        printf("Pas de racines réelles\n");
    }else if(discriminant(a,b,c) == 0){
        float x = - b / 2*a;
        printf("La racine double est %.2f\n", x);
    }else{
        float x= (- b + sqrt(discriminant(a,b,c))/2*a);
        float y= (- b - sqrt(discriminant(a,b,c))/2*a);
        printf("Les deux racines x et y sont %.2f et %.2f\n", x,y);
    }  
}

int signeProduit(int a, int b) {

if (a*b == 0) 
{ 
return 0;
}

if (a*b < 0) { 
    return -1;
}

return 1;
}

int main() {
  int a,b,c;
  
  scanf("%d",&a);
  scanf("%d",&b);
  scanf("%d",&c);
 
  printf("Racines de %d*x*x + %d*x + %d\n",a,b,c);
  afficheRacines(a,b,c);
 
  return 0;
}

