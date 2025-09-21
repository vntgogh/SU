int jours(int nb_conta, int pop, float pour_cent){
	float contas = 1;
	int jour = 0;
	while ((contas*100)/pop<pour_cent){
		contas = contas + (nb_conta*contas);
		jour++;
	}
	return jour;
}
