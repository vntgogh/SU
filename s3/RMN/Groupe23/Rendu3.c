#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <math.h>
#define N 100000

/*
    Saadi Dit Saada Yanis
    Yu Jerome 
    Harraoui Ines
    Karihila Nawad
*/




void eval_Horner_1(double a, double* coeff_f, int n, double* f_a) {
    int i;
    *f_a = coeff_f[n];

    for ( i = n-1; i >= 0; i-- ) {
        *f_a = *f_a * a + coeff_f[i];
    }
}

void eval_Horner_2(double a,double *coeff_f,int n, double *f_a,double *f_minus_a){
    double a2=a*a;
    double yi,yp;
    int i;
    if(n%2!=0){
        yi=coeff_f[n];
        yp=coeff_f[n-1];
        i=n-2;
    }else{
        yi=0;
        yp=coeff_f[n];
        i=n-1;
    }
    for(;i>=0;i-=2){
        yi=yi*a2+coeff_f[i];
        yp=yp*a2+coeff_f[i-1];
    }
    *f_a=yp+a*yi;
    *f_minus_a=yp-a*yi;
}


void mulpol (double *coeff_f, int n, double *coeff_g, int p, double *coeff_h, int *q){
    
    int k = 0;

    //multiplication des coeff f et g
    for (int i=0; i<n;i++){
        for (int j=0; j<p; j++){
            k = i + j;
            *(coeff_h + k) += *(coeff_f + i) * *(coeff_g + j); //addition des coeff de meme degré
        }
    }


    //affiche le polynome
    for (int i=*q; i>=0;i--){
         if((i<*q)&&(coeff_h[i]>=0)){ 
                printf("+"); 
        }
        printf("%.1f*x^%d",coeff_h[i],i); 
    }
    printf("\n");
}

void gauss_sp(double *a, double *b, int n){
    int i, j, k;
    float aux, aux2;
    for (i = 0; i<n-1; i++){
        aux = *(a + i*n + i);
        for (k = i+1; k<n; k++){
            *(a + i*n + k) /= aux;
        }
        *(b + i) /= aux;
        for (k = i+1; k<n; k++){
            aux2 = *(a + k*n + i);
            for (j = i+1; j<n; j++){
                *(a + k*n + j) -= aux2 * *(a + i*n + j);
            }
            *(b + k) -= aux2 * *(b+i);
        }
    }
    *(b + n-1) /= *(a + n*n -1);
    for (i = n-2; i>=0; i--){
        aux = *(b + i);
        for (k = i+1; k<n; k++){
            aux -= *(a + i*n + k) * *(b +k);
        }
        *(b + i) = aux;
    }
}

void vandermonde(double *a,double *vander,int n){
    int cpt=0;
    for (int i = 0; i<n; i++) {
        for ( int j = 0; j<n; j++ ) {
            *(vander + i*n +j) = 1;
            // printf("a = %d\n", *(a + cpt));
            if ( j > 0 ) {
                for ( int k = 1; k<=j ; k++) {
                    *(vander + i*n +j) *= *(a + cpt);
                }
            }
        }
        cpt++;
    }
    // for (int i = 0; i<n; i++) {
    //     for ( int j = 0; j<n; j++ ) {
    //         printf("%.1f\t",*(vander + i*n +j));
    //     }
    //     printf("\n");
    // }
}

void interpol_linalg( double *a, double *f_a,int n,double *coeff_f){
    
    int NN=(n+1)*(n+1);
    double* a_mat = malloc(sizeof(double)*NN);
    // Creation de la matrice
    vandermonde(a,a_mat,n);

    // //Copie de f_a  dans coeff_f
    for (int k = 0; k < n; k++){
        *(coeff_f + k) = *(f_a + k);
    }

    gauss_sp(a_mat, coeff_f, n);

    free(a_mat);

    
    // for (int i = 0; i<n; i++) {
    //     printf(" %f ",*(coeff_f + i));
    //     printf("\n");
    // }

    // for (int i = 0; i<n; i++) {
    //         printf(" %f ",*(f_a + i));
    //     printf("\n");
    // 
}


void interpol_Lagrange(double *a, double *f_a, int n, double *coeff_f){
    double newCoeff[n];
    double produit;

    // On initialise la liste des coeff à 0;
    for(int i = 0; i < n; i++)
        *(coeff_f+i) = 0.0;

    for(int i = 0; i < n; i++){
        produit = 1.0;

        // On initialise la liste des nouveaux coeff à 0 et on calcule le dénominateur de la formule des L_i;
        for(int j = 0; j < n; j++){
            newCoeff[j] = 0.0;
            if (i != j)
                produit *= *(a+i) - *(a+j);
        }

        if (produit == 0){
            printf("Division par zero : exit 1\n");
            exit(1);
        }
        produit = *(f_a+i) / produit;
        newCoeff[0] = produit;

        for(int j = 0; j < n; j++){
            if (i != j){
                for(int k = n-1; k > 0; k--){
                    newCoeff[k] += newCoeff[k-1];
                    newCoeff[k-1] *= -*(a+j);
                }
            }
        }

        // Nous mettons les nouveaux coefficients dans notre variable.
        for(int j = 0; j < n; j++)
            *(coeff_f + j) += newCoeff[j];
    }
}

void multpointeval_Horner1(double* coeff_f, double* a, int n, double *mulh1){
    // évalue le polynome f et retourne un tableau res de degré inférieur à 2n en 2n points
    // coeff_f= tableau de coefficients du polynome f de degré n
    // a= tableau des points de taille n

    //évaluation du polynome
    for(int i= 0; i < n; i++){
        eval_Horner_1(a[i],coeff_f,n,&mulh1[i]);
    }


}

void multpointeval_Horner2(double* coeff_f, double* a, int n, double ** mulh2){
    // évalue le polynome f et donne un tableau res de degré inférieur à 2n en 2n points en utilisant le schéma d'Horner d'ordre 2

    for(int i=0; i<n; i++){        
        double f_a, f_minus_a;
        eval_Horner_2(a[i], coeff_f,n, &f_a, &f_minus_a);
        mulh2[i][0]= f_a;        //image du x positif
        mulh2[i][1]= f_minus_a;  //image du x négatif
    }

    //affichage des valeurs du tableau
    // for(int i=0; i<n;i++){
    //     for(int j=0; j<2; j++){
    //         printf("mulh2[%d][%d] = %.1f\n",i,j, res[i][j]);
    //     }
    // }
}

void multpointeval_linalg(double *a,double *coeff_f, int n, double *res){
    int NN = (n + 1) * (n + 1);
    double a_mat[NN];

    vandermonde(a, a_mat, n);

    //résoud le système pour obtenir les coef du polynôme
    gauss_sp(a_mat, coeff_f, n);

    for(int i= 0;i<n;i++){
        res[i]=0.0;
        //calcule le polynôme au point x de a
        res[i]+=coeff_f[i]*pow(a[i], i); //coef multiplié par x puissance i
    }
}