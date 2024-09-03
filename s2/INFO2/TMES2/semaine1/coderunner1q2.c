void afficheRacines(int a, int b, int c) {
    int delta = discriminant(a, b, c);
    if (delta > 0) {
        float x1 = (-b + sqrt(delta)) / (2*a);
        float x2 = (-b - sqrt(delta)) / (2*a);
        printf("Les deux racines sont %.2f et %.2f", x1, x2);

    } else if (delta == 0) {
        float x = -b / (2*a);
        printf("La racine double est %.2f", x);

    } else {
         printf("Pas de racine reelle\n");

    }
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
