#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <math.h>
#include "Rendu3.h"


int main(){
    srand(time(NULL));

    int n = 4;
    double t = 0.0;
    double t1 = 0.0;

    double *f_a=malloc(sizeof(double)*n);
    double *f_aLinalg=malloc(sizeof(double)*n);

    double *coeff_f=malloc(sizeof(double)*n);
    double *coeff_fLinalg=malloc(sizeof(double)*n);
    
    for ( int i = 0; i<n; i++ ) {
        coeff_f[i] = -1+2*((double)rand())/RAND_MAX;
    }



    for ( int i = 0; i<n; i++ ) {
        *(coeff_fLinalg+i) = -1+2*((double)rand())/RAND_MAX;
    }

    double a_tab[n];

    for(int i=0;i<n;i++){
        a_tab[i]=(double)i+1;
    }

    for(int i=0;i<n;i++){
        *(f_a+i)=(double)((rand()%4)-4);
    }


     //Test multipointeval_Horner1

    printf("multpointeval_Horner1\n");
    double *mulh1=(double *)malloc(sizeof(double)*n);
    
    
    multpointeval_Horner1(coeff_f,a_tab,n, mulh1);

    //affichage des valeurs du tableau
    for (int i= 0; i<n; i++){
        printf("res[%d] = %.1f\n", i, mulh1[i]);
    }

    //Test multipointeval_Horner2

    
    printf("multpointeval_Horner2\n");
    double **mulh2 = (double **)malloc(sizeof(double *)*n); //tableau de n tableaux de taille 2, avec n, la taille du tableau de points
    for(int i=0; i < n; i++){
        mulh2[i]=(double *)malloc(sizeof(double)*2);//2 tableaux: un pour les points positifs et un pour les négatifs
    }
    multpointeval_Horner2(coeff_f,a_tab,n,mulh2);

    for(int i=0; i<n;i++){
        for(int j=0; j<2; j++){
            printf("mulh2[%d][%d]= %.1f\n",i,j,*(*(mulh2+i)+j));
        }
    }


    	int entier_mult;
    printf("Tapez un entier i entre 0 et 16 (2^i) : "); scanf("%d",&entier_mult);






    //Test multipointeval_linalg

    printf("multpointeval_linalg\n");

    multpointeval_linalg(a_tab,coeff_fLinalg,n,f_aLinalg);
    
    for(int i=0;i<n;i++){
        printf("coeff_fLinalg[%d]=%f\n",i,*(f_aLinalg+i));
    }

    free(f_a);
    free(f_aLinalg);
    free(coeff_f);
    free(coeff_fLinalg);
    for(int i= 0; i< n; i++){
        free(*(mulh2+i));
    }
    free(mulh1);
    free(mulh2);


    {
    // Degré 2^i
	int deg_mult = 1;
    for ( int i = 0; i<entier_mult; i++ ){
        if ( entier_mult > 0 ) {
            deg_mult *= 2;
        }
    }
    double *mulh1=(double *)malloc(sizeof(double)*deg_mult);
    double **mulh2 = (double **)malloc(sizeof(double *)*deg_mult); //tableau de n tableaux de taille 2, avec n, la taille du tableau de points
    double *mulcoeff_f=(double *)malloc(sizeof(double)*deg_mult);
    double *mulf_a=(double*)malloc(sizeof(double)*deg_mult);
    double t_mult = 0.0;
    double t1_mult = 0.0;
    double t2_mult = 0.0;
    double coeff_f[deg_mult];

    double a_tab[deg_mult];
    for(int i=0;i<deg_mult;i++){
        a_tab[i]=(double)i+1;
    }
    // Liste de coefficient avec des valeurs aléatoire de [-1;1]
    for ( int j = 0; j<deg_mult; j++ ) {
        coeff_f[j] = -1+2*((float)rand())/RAND_MAX;
    }
    for(int i=0;i<deg_mult;i++){
        *(mulcoeff_f+i)=-1+2*((double)rand())/RAND_MAX;
    }
    for(int i=0; i < deg_mult; i++){
        mulh2[i]=(double *)malloc(sizeof(double)*2);//2 tableaux: un pour les points positifs et un pour les négatifs
    }


	time_t debut_mult = clock();
    multpointeval_Horner1(coeff_f,a_tab,deg_mult, mulh1);
	time_t fin_mult = clock();
    t_mult += (fin_mult - debut_mult) / CLOCKS_PER_SEC;
	time_t timeHorner1 = (fin_mult - debut_mult)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de eval_Horner_1() pour n = 2^%d est de %ld ms\n", entier_mult, timeHorner1);

	debut_mult = clock();
    multpointeval_Horner2(coeff_f,a_tab,deg_mult,mulh2);
	fin_mult = clock();
    t1_mult += (fin_mult - debut_mult) / CLOCKS_PER_SEC;
	time_t timeHorner2 = (fin_mult - debut_mult)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de eval_Horner_2() pour n = 2^%d est de %ld ms\n\n", entier_mult, timeHorner2);

	debut_mult = clock();
    multpointeval_linalg(a_tab,mulf_a ,deg_mult,mulcoeff_f);
	fin_mult = clock();
    t2_mult += (fin_mult - debut_mult) / CLOCKS_PER_SEC;
	time_t timeLinalg = (fin_mult - debut_mult)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de multipointeval_linalg() pour n = 2^%d est de %ld ms\n\n", entier_mult, timeLinalg);

    if ( t_mult < t1_mult ) {
        if ( t_mult < t2_mult ) {
            printf("multpointeval_Horner1 est plus rapide que multpointeval_Horner2 de %f\n\n", t1_mult-t_mult);
        } else {
            printf("multpointeval_Horner1 est plus rapide que multpointeval_Horner2 de %f\n\n", t2_mult-t_mult);
        }
    } else {
        if ( t1_mult < t2_mult ) {
            printf("multpointeval_Horner2 est plus rapide que multpointeval_Horner1 de %f\n\n", t2_mult-t1_mult);
        } else {
            printf("multpointeval_Horner2 est plus rapide que multpointeval_Horner1 de %f\n\n", t1_mult-t2_mult);
        }
    }

    free(mulh1);
    for(int i= 0; i< n; i++){
        free(*(mulh2+i));
    }
    free(mulh2);
    free(mulf_a);
    free(mulcoeff_f);
}
}