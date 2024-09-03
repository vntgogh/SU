#include <stdio.h>
#include <math.h>
int discriminant(int a , int b, int c){
  return b*b-(4*a*c);
}

int nb_racines(int a, int b , int c){
  int d = discriminant(a,b,c);
  if (d<0){
    return 0;
  }if(d==0){
    return 1;
  }else{
    return 2;
  }
}


float racines(int a , int b , int c, float *x1, float *x2, float *x){
  int d = discriminant(a,b,c);
  int n = nb_racines(a,b,c);
  if (n==1){
    *x= ((-b+0.0)/(2*a));
    printf("%.2f\n", *x);
  }if (n==2){
    *x1= ((-b+0.0) - sqrt(d))/(2*a);
    *x2= ((-b+0.0) + sqrt(d))/(2*a);
    printf("%.2f, %.2f\n", *x1,*x2);
  }if(n==0){
    printf("pas de racines reelles\n");
  }  
}

int main(){
  int a=2, b=9, c=4;
  float r1,r2, r;
  racines(a,b,c,&r1,&r2, &r);
}