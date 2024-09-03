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
    double *coeff_f=malloc(sizeof(double)*n);
    double *coeff_f2=malloc(sizeof(double)*n);

    double a_tab[n];

    for(int i=0;i<n;i++){
        a_tab[i]=(double)i+1;
    }

    for(int i=0;i<n;i++){
        *(f_a+i)=(double)((rand()%4)-4);
    }

    //Test Exercice 3.1
    interpol_linalg(a_tab,f_a,n,coeff_f);

    printf("Interpol Linalg : \n");
    for (int i = 0; i<n; i++) {
        printf(" %f ",*(coeff_f + i));
        printf("\n");
    }

    //Test Exercice 3.2


    interpol_Lagrange(a_tab,f_a,n,coeff_f2);

    printf("Interpol Lagrange : \n");
    for (int i = 0; i<n; i++) {
        printf(" %f ",*(coeff_f2 + i));
        printf("\n");
    }

    // Test Exercice 3.3

  int entier_interpole;
    printf("\nTapez un entier i entre 0 et 16 (2^i) : "); scanf("%d",&entier_interpole);

    // Degré 2^i
	int deg_interpole = 1;
    for ( int i = 0; i<entier_interpole; i++ ){
        if ( entier_interpole > 0 ) {
            deg_interpole *= 2;
        }
    }
    printf("%d\n", deg_interpole);
	double *a_interpole = malloc(sizeof(double)*deg_interpole);
	double *f_a_interpole = malloc(sizeof(double)*deg_interpole);
    double coeff_f_interpole[deg_interpole];
    double t_interpole = 0.0;
	double t1_interpole = 0.0;

    // Liste de a et f_a avec des valeurs aléatoire de [-1;1]
	for(int i = 0; i < deg_interpole; i++){
		*(a_interpole+i) = ((double)rand()*2) / (double)RAND_MAX - 1;
		*(f_a_interpole+i) = ((double)rand()*2) / (double)RAND_MAX - 1;
	}

	time_t debut_interpole = clock();
	interpol_linalg(a_interpole, f_a_interpole, deg_interpole, coeff_f_interpole);
	time_t fin_interpole = clock();
    t_interpole += (double)(fin_interpole - debut_interpole) / CLOCKS_PER_SEC;
	time_t timeLinalg = (fin_interpole - debut_interpole)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de interpol_linalg() pour n = 2^%d est de %ld ms\n", entier_interpole, timeLinalg);

	debut_interpole = clock();
	interpol_Lagrange(a_interpole, f_a_interpole, deg_interpole, coeff_f_interpole);
	fin_interpole = clock();
    t1_interpole += (double)(fin_interpole - debut_interpole) / CLOCKS_PER_SEC;
	time_t timeLagrange = (fin_interpole - debut_interpole)*1000/CLOCKS_PER_SEC;
	printf("\nLe temps de calcul de interpol_lagrange() pour n = 2^%d est de %ld ms\n\n", entier_interpole, timeLagrange);

    if ( t_interpole < t1_interpole )
    printf("interpol_linalg est plus rapide que interpol_Lagrange de %f\n\n", t1_interpole-t_interpole);
    else
    printf("interpol_Lagrange est plus rapide que interpol_linalg de %f\n\n", t_interpole-t1_interpole);

    free(a_interpole);
    free(f_a_interpole);

    free(f_a);
    free(coeff_f);
    free(coeff_f2);

}