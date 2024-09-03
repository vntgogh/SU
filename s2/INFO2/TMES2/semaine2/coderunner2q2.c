#include <math.h>
float pourcentage(int nb_conta, int pop, int jour){
	float contas = 1.0;
	for (int i=1; i<=jour; i++){
		contas = contas + (nb_conta*contas);
	}
	return fmin((contas*100)/pop, 100.0);
}
