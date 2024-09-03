#include <stdio.h>
#include <cini.h>

void diagonale(int x){
  for (int i=0; i<x; i++){
    CINI_draw_pixel(i, i, "orange"); //x=y
  }
}

void carre(int x, int y, int l){
  for (int i=0; i<l; i++){
   CINI_draw_pixel(x+i, l, "green");
   CINI_draw_pixel(l, y+i, "black");
   CINI_draw_pixel(x, y+i, "red");
   CINI_draw_pixel(x+i, y, "blue");
  }
}

void carre_remontant(int x, int y, int l){
  while (x!=0 || y!=0){
    carre(x,y,l);
    x-=20;
    y-=20;
  }
}

int position(int a, int b, int x, int y){
  int m = a*x+b;
  if (y== m){
    return 0;
  }if(y<m){
    return 1;
  }else{
    return -1;
  }
}

void affiche(int a, int b, int h, int l){
  for(int i=0;i<l;i++){ //parcourir tous les
    for (int j=0;j<h;j++){ //points de la fenetre
      if (position(a,b,i,j)==1){
        CINI_draw_pixel(i, j, "red");
      }if (position(a,b,i,j)==-1){
        CINI_draw_pixel(i, j, "blue");
      }else{
        CINI_draw_pixel(i, j, "black");
      }
    }
  }
}

int main() {
    CINI_open_window(400, 300, tme2);
    CINI_fill_window("white");
    affiche(1,2,50,150);
    CINI_loop();
    return 0;
}
