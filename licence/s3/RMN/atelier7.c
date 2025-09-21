#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <stdint.h>
#include <stdbool.h>

#define N 100000


// exercice 1
//On applique la formule de la vidéo mais en log base
//On passe en log base 2 car on cherche à renvoyer le nombre de bits communs
//Donc on regarde nos réels base 10 en base 2
//D'où passer de log10 à log2
//cependant les arrondis en C ne permettent pas à bitcommun d'afficher les bons résultats

int bitcommun(double x, double y){
    return -log(fabs(2*(x-y)/(x+y)))/log(2); 
}

//convertit les nombres en entiers 64 bits pour accéder directement à leurs bits
int bitcommun_opt(double x, double y){

    uint64_t a = *(uint64_t*)&x;
    uint64_t b = *(uint64_t*)&y;
    
    
    int cmp = 0;
    //k = 51 car on est sur un format double précision (64 bits)
    //k = 51 car la mantisse va de 52 à 0, donc le bit le plus fort est à la 51ème position
    int k = 51;

    //S'arrête quand le bit à la position k de a est différent du bit à la position k 
    //de b 
    //On utilise "1ull" et pas "1u" car on manipule un entier non signé 64 bits
    while ((a & (1ull << k)) == (b & (1ull << k)) && k >= 0){
        cmp++;
        k--;
    }
    
    //On ajoute le bit caché
    return cmp + 1;
}


//exercice 2

// programme qui renvoie tous les premiers termes tels que la différence entre 
// chaque terme et le terme qui le précède est supérieure à epsilon
double dpeps(double alpha, double xn, double eps) {

    // double alpha,eps,xn;
    // printf("Entrez alpha, x et epsilon : \n");
    // scanf("%lf", &alpha);
    // scanf("%lf", &xn);
    // scanf("%lf", &eps);
    printf("x0 = %.2f\n", xn);

    double x_suiv=(((4*xn - (3*alpha-2))*xn-alpha)*xn-2*alpha)/((5*xn-(4*alpha -3))*xn-2*alpha-2);
    printf("x1 = %.14f\n", x_suiv);
    int i=1;
    // la suite converge si la valeur absolue de cette différence devient inférieure à epsilon
    while(fabs(xn-x_suiv)> eps){ 
        xn=x_suiv; // terme precedent
        double xn1=(((4*xn - (3*alpha-2))*xn-alpha)*xn-2*alpha);
        double xn2=((5*xn-(4*alpha -3))*xn-2*alpha-2);
        x_suiv=xn1/xn2; // terme courant
        i++;
        printf("x%d = %.14f\n", i, x_suiv);
        
    }
    return x_suiv;
}

/*double horner(double x, int n, double *p){
    double r= p[n];
    for (int i= n-1; i>= 0; i--) {
        r+=r*x+p[i];
    }
    return r;
}*/

double horner(double x, int n, double *p){
    double r = x * p[n] + p[n-1];
    for (int i= n-2; i > 0; i--) {
        r += x * r + p[i];
    }
    return r + p[0];
}

double dpeps2(double alpha, double xn, double eps){
    /*double alpha,eps,xn;
    printf("Entrez alpha, x et epsilon : \n");
    scanf("%lf", &alpha);
    scanf("%lf", &xn);
    scanf("%lf", &eps);*/
    
    double p1[4]={-2*alpha, -alpha, -(3*alpha-2), 4}; //{4,-(3*alpha-2),-alpha,-2*alpha};
    double p2[3]={-(2*alpha+2), -(4*alpha-3), 5}; //{5,-(4*alpha-3), -2*alpha-2};
    double x_suiv=horner(xn,4,p1)/horner(xn,3,p2);

    printf("x0 = %.14f\n", xn);
    printf("x1 = %.14f\n", x_suiv);
    int i=1;
    while(fabs(xn-x_suiv)>eps){
        xn=x_suiv; 
        i++;
        printf("x%d = %.14f\n", i, x_suiv);

        double xn1=horner(xn,4,p1);
        double xn2=horner(xn,3,p2);
        x_suiv=xn1/xn2;
    }
    return x_suiv;
}

int main(){

    // exercice 1

    // printf("%d\n",bitcommun_opt(1.41421356, 1.41427845));
    // printf("%d\n",bitcommun_opt(9.87452334, 9.87901342));
    // printf("%d\n",bitcommun_opt(10.07452334, 10.07901342));
    // printf("%d\n",bitcommun_opt(-2.69998756, -2.70001234));
    
    assert(bitcommun_opt(1.41421356, 1.41427845)==14);
    assert(bitcommun_opt(9.87452334, 9.87901342)==6);
    assert(bitcommun_opt(10.07452334, 10.07901342)==9);
    assert(bitcommun_opt(-2.69998756, -2.70001234)==15);  

    // exercice 2
    
    //dpeps(0.3,2,0.001);
    //dpeps(0.3,2,pow(10,-14));
    //dpeps(3.5,5,pow(10,-14));
    //dpeps(3.5,0.5,pow(10,-14));
    //dpeps(1.0,-3.0,pow(10,-14));
    //dpeps(1.0,2.0,pow(10,-14));

    dpeps2(0.3,2,0.001);
    //dpeps2(0.3,2,pow(10,-14));
    //dpeps2(3.5,5,pow(10,-14));
    //dpeps2(3.5,0.5,pow(10,-14));
    //dpeps2(1.0,-3.0,pow(10,-14));
    //dpeps2(1.0,2.0,pow(10,-14));

    return 0;
}