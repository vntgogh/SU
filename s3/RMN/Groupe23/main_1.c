#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <math.h>
#include "Rendu3.h"


int main(){
    srand(time(NULL));
    /*Initialisation des variables pour les test des eval_horner*/

    int n = 4;
    double a = 2.0;
    double f_a=0.0;
    double f_a2;
    double f_minus_a2;
    double coeff_f[n];

    int len1=(int)((rand()%4)+1);
    int len2=(int)((rand()%4)+1);
    double f[len1];
    double g[len2];

    for(int i=0;i<len1;i++){
        *(f+i)=(double)((rand()%8)-4);
    }  

    for(int i=0;i<len2;i++){
        *(g+i)=(double)((rand()%8)-4);
    }

    int df = len1-1;
    int dg = len2-1;
    int q=df+dg+1;

    double *h=malloc(sizeof(double)*q);
    




    for ( int i = 0; i<n; i++ ) {
        coeff_f[i] = -1+2*((double)rand())/RAND_MAX;
    }
    /*Test pour eval_Horner 1*/

    eval_Horner_1(a, coeff_f, n, &f_a);
    printf("f_a = %f\n", f_a);

    // Test eval_Horner_2

    eval_Horner_2(a, coeff_f, n, &f_a2, &f_minus_a2);
    printf("f_a2 = %f ; f_minus_a2= %f \n", f_a2,f_minus_a2);


    //Test mul_pol

        mulpol(f,df,g,dg,h,&q);
    
    //Test Exercice 1.3

    int entier_Horner;
    printf("\nTapez un entier i entre 0 et 16 (2^i) : "); scanf("%d",&entier_Horner);

    // Degré 2^i
	int deg_Horner = 1;
    for ( int i = 0; i<entier_Horner; i++ ){
        if ( entier_Horner > 0 ) {
            deg_Horner *= 2;
        }
    }
    double a_Horner = 2.0;
    double f_a_Horner, f_a2_Horner;
    double f_minus_a;
    double t = 0.0;
    double t1 = 0.0;
    double coeff_f_Horner[deg_Horner];

    // Liste de coefficient avec des valeurs aléatoire de [-1;1]
    for ( int j = 0; j<deg_Horner; j++ ) {
        coeff_f_Horner[j] = -1+2*((float)rand())/RAND_MAX;
    }

	time_t debut = clock();
	eval_Horner_1(a_Horner, coeff_f_Horner, deg_Horner, &f_a_Horner);
	time_t fin = clock();
    t += (fin - debut) / CLOCKS_PER_SEC;


	time_t timeHorner1 = (fin - debut)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de eval_Horner_1() pour n = 2^%d est de %ld ms\n", entier_Horner, timeHorner1);

	debut = clock();
	eval_Horner_2(a_Horner, coeff_f_Horner, deg_Horner, &f_a2_Horner, &f_minus_a);
	fin = clock();
    t1 += (fin - debut) / CLOCKS_PER_SEC;

	time_t timeHorner2 = (fin - debut)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de eval_Horner_2() pour n = 2^%d est de %ld ms\n\n", entier_Horner, timeHorner2);

    if ( t < t1 ){
        printf("eval_Horner_1 est plus rapide que eval_Horner_2 de %.10f\n\n", t1-t);

    }else{
        printf("eval_Horner_2 est plus rapide que eval_Horner_1 de %.10f\n\n", t-t1);
    }

    free(h);


    return 0;
}