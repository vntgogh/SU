#include <stdio.h>
#include <math.h>
#define TFAMILLE 57.8
#define TADULTE 22.7
#define TENFANT 10.75

float prixEntree (int adultes, int enfants){
	float prix;
	int t_enfants = enfants/3;
	enfants = enfants%3;
	int d_adultes = adultes/2;
	adultes = adultes%2;
	prix = fmin(t_enfants,d_adultes)*TFAMILLE;
	enfants = enfants + 3*(t_enfants-fmin(t_enfants,d_adultes));
	adultes = adultes + 2*(d_adultes-fmin(t_enfants,d_adultes));
	prix = prix + fmin(adultes*TADULTE + enfants *TENFANT, (adultes-fmin(adultes,2))*TADULTE + (enfants-fmin(enfants,3))*TENFANT + TFAMILLE);
	return prix;
}

int main() {
  int nb_a, nb_e;

  scanf("%d",&nb_a);
  scanf("%d",&nb_e);

  printf("(%d adulte(s), %d enfant(s)) = %.2f livres\n",nb_a,nb_e,prixEntree(nb_a,nb_e));

  return 0;
}
