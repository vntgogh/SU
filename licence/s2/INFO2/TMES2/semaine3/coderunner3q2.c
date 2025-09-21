#include <stdio.h>

void echange( int *x ,  int *y){
    int c = *x;
    *x = *y;
    *y = c;
}

void tri_croissant(int *x, int *y){
    if (*x>*y){
        echange(x,y);
    }
}

void tri_3( int *x, int *y, int *z){
    while (!((*x<=*y)&&(*y<=*z))){
        if (*x >=*y) {
            tri_croissant(x,y);
        }
        if (*y >=*z) {
            tri_croissant(y,z);
        }
    }
}

int main() {
   int a, b, c;

   printf("Saisissez les valeurs de a, b et c :\n");
   scanf("%d", &a);
   scanf("%d", &b);
   scanf("%d", &c);
   printf("Avant echange : a = %d, b = %d\n",a, b);
   echange(&a,&b);
   printf("Apres echange : a = %d, b = %d\n",a, b);

   tri_croissant(&a,&b);
   printf("Par ordre croissant : a = %d, b = %d\n", a, b);

   tri_3(&a,&b,&c);
   printf("Apres tri : a = %d, b = %d, c = %d\n",a, b, c);

   return 0;
}
