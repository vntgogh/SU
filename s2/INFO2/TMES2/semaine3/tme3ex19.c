#include <stdio.h>
#include <stdlib.h>

void min_max(int x, int *min, int *max){
  if(x<*min){
    *min=x;
  }if(*max<x){
    *max=x;
  }
}

void stats(int a,int b, int c, int d, int *min, int *max, float *moy){
  int l=0;
  if (a<0){
    *min=-1;
    *max=-1;
    *moy=-1.0;
  }else{
    min_max(a, min,max);
    *moy+=a;
    l++;
    if(b>0){
      min_max(b, min,max);
      *moy+=b;
      l++;
      if(c>0){
        min_max(c, min,max);
        *moy+=c;
        l++;
        if(d>0){
          min_max(d, min,max);
          *moy+=d;
          l++;
        }
      }
    }
  } *moy= *moy/l;
}
int main(){
  int a=-2;
  int mi=0, ma=5;
  //min_max(a,&mi,&ma);
  //printf("%d,%d\n",mi,ma);
  int v1=-2, v2=-7, v3=-5, v4=9;
  int m=2, M=2;
  float mo=0.0;
  stats(v1,v2,v3,v4,&m,&M,&mo);
  printf("%d,%d,%.2f\n", m, M, mo);
}