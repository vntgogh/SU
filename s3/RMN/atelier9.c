#include <stdlib.h>
#include <stdio.h>
#include <math.h>

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
    printf("f_a= %.1f, f_minus_a = %.1f\n", *f_a, *f_minus_a);
}

void mulpol(double* coeff_f, int n, double* coeff_g, int p,double* coeff_h, int* q){
    //calcule le produit h des polynômes f et g respectivement de degrés n et p

    for(int i=0; i<*q;i++){
        coeff_h[i]=0;
    }

    for (int i=0; i<=n;i++){ //parcourt les coef de f et de g et les multiplie entre eux
        for (int j=0; j<=p; j++){
            coeff_h[i+j]+= coeff_f[i]*coeff_g[j]; //h[i+j] additionne les coef de meme degré
        }
    }

    //affiche le polynome
    for (int i=*q; i>=0;i--) {
        if((i<*q)&&(coeff_h[i]>=0)){ 
                printf("+"); //affiche "+"" si le coef est positif(le "-" s'affiche de lui-meme si le coef est négatif)
        }
        printf("%.1f*x^%d",coeff_h[i],i); 
    }
}

void multpointeval_Horner1(double* coeff_f, double* a, int deg_f, int n, double *res){
    // évalue le polynome f et retourne un tableau res de degré inférieur à 2n en 2n points
    // coeff_f= tableau de coefficients du polynome f de degré deg_f
    // a= tableau des points de taille n

    //évaluation du polynome
    for(int i= 0; i < n; i++){
        eval_Horner_1(a[i],coeff_f,deg_f,&res[i]);
    }

    //affichage des valeurs du tableau
    // for (int i= 0; i<n; i++){
    //     printf("res[%d] = %.1f\n", i, res[i]);
    // }
}

void multpointeval_Horner2(double* coeff_f, double* a, int deg_f, int n, double ** res){
    // évalue le polynome f et retourne un tableau res de degré inférieur à 2n en 2n points en utilisant le schéma d'Horner d'ordre 2

    for(int i=0; i<n; i++){        
        double f_a, f_minus_a;
        eval_Horner_2(a[i], coeff_f, deg_f, &f_a, &f_minus_a);
        res[i][0]= f_a;        //image du x positif
        res[i][1]= f_minus_a;  //image du x négatif
    }

    //affichage des valeurs du tableau
    for(int i=0; i<n;i++){
        for(int j=0; j<2; j++){
            printf("res[%d][%d] = %.1f\n",i,j, res[i][j]);
        }
    }
}

void gauss_sp(double* a, double *b, int n){
    int i, j, k;
    double aux, aux2;
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
    for (int i = 0; i<n; i++) {
        for ( int j = 0; j<n; j++ ) {
            printf("%.1f\t",*(vander + i*n +j));
        }
        printf("\n");
    }
}

void interpol_linalg( double *a, double *f_a,int n,double *coeff_f){
    
    int NN=(n+1)*(n+1);
    double a_mat[NN];
    // Creation de la matrice 
    vandermonde(a,a_mat,n);
    
    //Copie de f_a  dans coeff_f

    for (int k = 0; k < n; k++){
        *(coeff_f + k) = *(f_a + k);
    }

    gauss_sp(a_mat, coeff_f, n);
    
    // for (int i = 0; i<n; i++) {
    //     printf(" %f ",*(coeff_f + i));
    //     printf("\n");
    // }

    // for (int i = 0; i<n; i++) {
    //         printf(" %f ",*(f_a + i));
    //     printf("\n");
    // }
}

void multpointeval_linalg(double *a,double *f_a, int n, double *coeff_f){
    //évalue un polynôme dans un tableau de coefficients en utilisant un produit de matrice-vecteur

    int NN=(n+1)*(n+1);
    double a_mat[NN];
    // Creation de la matrice 
    vandermonde(a,a_mat,n);

    //Copie de f_a  dans coeff_f

    for (int k = 0; k < n; k++){
        *(coeff_f + k) = *(f_a + k);
    }

    gauss_sp(a_mat, coeff_f, n);
    
    //initialisation des polynomes à 0 
    for(int i=0;i<n;i++){
        coeff_f[i]=0;
        for(int j=0; j<=n;j++){
            coeff_f[i]+=*(a_mat+i+j)*a[i]; //calcul du polynome au point (i, j) de la matrice a_mat
        }
    }

    //affichage du polynome de chaque point
    for (int i=0; i<n; i++){
        printf("coeff_f[%d] = %.1f\n", i, coeff_f[i]);
    }
}

void interpol_Lagrange(double* a, double* f_a, int n, double* coeff_f){
    for(int i=0;i<n;i++){
        *(coeff_f+i)=*(f_a+i);
        for (int j=0; j<n;j++){
            if(j!=i){
                *(coeff_f+i)/=(*(a+i)- *(a+j));
            }
        }
    }
}

int main(){
    double f[]={1,-3,2}; //coefficents d'un polynome du second degre
    // double g[]={1,-2};
    // int df = 2, dg = 1, q=df+dg+1; 

    // double *h=malloc(q*sizeof(double));  
    // mulpol(f,df,g,dg,h,&q);
    // printf("\n");


    double a[]={1,2,-1,-2}; //tableau des x1 à xn
    int n=4;
    //int deg_f=3; // n est le degré de a
    // double *res=(double *)malloc(sizeof(double)*n);
    // multpointeval_Horner1(f,a,deg_f,n, res);


    // double **res2 = (double **)malloc(sizeof(double *)*n); //tableau de n tableaux de taille 2, avec n, la taille du tableau de points
    // for(int i=0; i < n; i++){
    //     res2[i]=(double *)malloc(sizeof(double)*2);//2 tableaux: un pour les points positifs et un pour les négatifs
    // }
    // multpointeval_Horner2(f,a,deg_f,n,res2);


    // double fa, fminusa;
    // eval_Horner_2(a[2],f,3, &fa,&fminusa);

    double f_a[]={4,8,-4,-8};
    double coeff_f;
    double *mult_coeff_f=(double *)malloc(sizeof(double)*n);

    interpol_linalg(a,f_a,4,&coeff_f);
    printf("\n");

    multpointeval_linalg(a, f_a, n,mult_coeff_f);

    interpol_Lagrange(a,f_a,n,&coeff_f);
    printf("%.1f", coeff_f);

    // free(h); 
    // free(res);
    // for(int i= 0; i< n; i++){
    //      free(res2[i]);
    // }
    // free(res2);
    // free(res3);
    
    return 0;
}