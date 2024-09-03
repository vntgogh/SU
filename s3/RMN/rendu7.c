#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <time.h>

#define N 100000

//bit_commun calcule le nombre de bit en commun entre x et y
//On le calcule avec la fonction log en base 2
//cependant les arrondis en C ne permettent pas à bitcommun d'afficher les bons résultats

double bit_commun(double x, double y){

    double c = -log10(fabs((2*(x-y)) / (x+y)));

    return c;
}

//bitcommun_opt fait la même chose, mais on regarde cette fois bit à bit avec un décalage et un mask
double bitcommun_opt(double x, double y){

    //On convertit les nombres en entiers 64 bits pour accéder directement à leurs bits
    uint64_t a = *(uint64_t*)&x;
    uint64_t b = *(uint64_t*)&y;
    
    //On crée notre compteur à 1, car on pend en compte que le bit caché vaut 1 pour tout binaire
    double cmp = 1;

    //Pour compter les bits en commun on compare les bits de la mantisse des deux nombres
    //Lorsqu'on est sur 64 bits, la mantisse commence au 51e bits
    int k = 51;

    //On parcourt nos nombres bit à bit avec un décalage et un mask: n & (1ull << k)
    //On utilise "1ull" au lieu de "1u" lors qu'on manipule les entiers non signés
    while (( (a & (1ull << k)) == (b & (1ull << k)) ) ){
        cmp++;
        k--;
    }
    
    return cmp;
}

//deps renvoie tous les premiers termes tels que la différence entre chaque terme et le terme qui le précède est supérieure à epsilon
double dpeps() {

    double alpha,eps,xn;
    printf("Entrez alpha, x et epsilon : \n");
    scanf("%lf", &alpha);
    scanf("%lf", &xn);
    scanf("%lf", &eps);
    printf("x0 = %.2f\n", xn);

    double x_suiv=(((4*xn - (3*alpha-2))*xn-alpha)*xn-2*alpha)/((5*xn-(4*alpha -3))*xn-2*alpha-2);

    printf("x1 = %.14f\n", x_suiv);
    int i=1;
    while(fabs(xn-x_suiv)> eps){
        //xn est le terme précedent
        xn=x_suiv; 
         
        double xn1=(((4*xn - (3*alpha-2))*xn-alpha)*xn-2*alpha);
        double xn2=((5*xn-(4*alpha -3))*xn-2*alpha-2);

        //On calcule le terme courant
        x_suiv=xn1/xn2;
        i++;

        printf("x%d = %.14f\n", i, x_suiv);
        
    }
    return x_suiv;
}



int main(){

    //Exercice 1

    printf("Pour x = %f et y = %f:\n", 1645.9867 , 1645.9967 );
    printf("bit commun: %.2f\n", bit_commun(1645.9867, 1645.9967));

    printf("Pour x = %f et y = %f:\n", 9.98576364 , 9.98543231 );
    printf("bit commun: %.2f\n", bit_commun(9.98576364, 9.98543231 ));

    printf("Pour x = %f et y = %f:\n", 5.29999452 , 5.30000125  );
    printf("bit commun: %.2f\n", bit_commun(5.29999452 , 5.30000125 ));

    // printf("Pour x = %f et y = %f:\n",1.41421356, 1.41427845);
    // printf("bit commun: %d\nbit commun optimisé: %d\n", bit_commun(1.41421356, 1.41427845), bitcommun_opt(1.41421356, 1.41427845));

    // printf("Pour x = %f et y = %f:\n",9.87452334, 9.87901342);
    // printf("bit commun: %d\nbit commun optimisé: %d\n", bit_commun(9.87452334, 9.87901342), bitcommun_opt(9.87452334, 9.87901342));

    // printf("Pour x = %f et y = %f:\n",10.07452334, 10.07901342);
    // printf("bit commun: %d\nbit commun optimisé: %d\n", bit_commun(10.07452334, 10.07901342), bitcommun_opt(10.07452334, 10.07901342));

    // printf("Pour x = %f et y = %f:\n",-2.69998756, -2.70001234);
    // printf("bit commun: %d\nbit commun optimisé: %d\n", bit_commun(-2.69998756, -2.70001234), bitcommun_opt(-2.69998756, -2.70001234));

    //Temps de calculs
    // double x[N], y[N], un = 1;

    // for (int i = 0; i < N; i++){
    //     x[i] = (un * rand() * 10000) / RAND_MAX;
    //     y[i] = x[i] + (un * rand() * 0.0001) / RAND_MAX;
    // }

    // clock_t debut = clock();

    // for (int j = 0; j < N; j++){
    //     bit_commun(x[j], y[j]);
    //     // bitcommun_opt(x[j], y[j]);
    // }

    // clock_t fin = clock();

    // printf("TEMPS DE CALCUL %f\n", (double)(fin - debut) / CLOCKS_PER_SEC);

    // printf("\n\n");
    // //Exercice 2
    // dpeps();

    return 0;
}