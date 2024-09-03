#include <stdio.h>

void ma_fonction (int a, int b) {
    int c1,c2;
    int *d;

    c1= a+b;
    d=&a;
    *d = *d +2;
    c2= a+b;

    printf("a=%d, b=%d, c1 = %d, c2= %d, *d = %d\n",a,b,c1,c2,*d);

}

 int main() {
    int a=7, b=10;

    printf(" Avant appel : a=%d, b=%d\n",a,b);
    ma_fonction(a,b);
    printf(" Apres appel : a=%d, b=%d\n",a,b);
    return 0;
}
