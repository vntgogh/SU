#include <stdio.h>
#include <math.h>
#define TFAMILLE 57.8
#define TADULTE 22.7
#define TENFANT 10.75


float  prixEntree(int nb_a , int  nb_e){
    float res = nb_a * 22.7 + nb_e * 10.75;
    float prixAvecFamille = 57.8;
    if (nb_a   <= 2 &&nb_e <= 3 ) {
            return fmin(res, prixAvecFamille);
    } if (nb_a   > 2 &&nb_e >= 3 ) {
        return 57.8 + ((nb_a-2)*22.7) +((nb_e-3)*10.75);

    } else {
            return res ;
        }
}



int main() {
  int nb_a, nb_e;

  scanf("%d",&nb_a);
  scanf("%d",&nb_e);

  printf("(%d adultes, %d enfants) = %.2f livres\n",nb_a,nb_e,prixEntree(nb_a,nb_e));

  return 0;
}
