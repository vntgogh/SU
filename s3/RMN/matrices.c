#include <stdlib.h>
#include <stdio.h>

#define N 20

//Version par valeur 
float pscal_val(float v[], float w[]){
    int i;
    float pscal=0;
    for(i=0; i<n;i++){
        pscal+= v[i]*w[i]; //v + 4*i et w+ 4*i à chaque itération
    }
    return pscal;
}

//Version par adresse

float pscal_adresse(float *v, float *w){
    float pscal=0;
    v=malloc(sizeof(float)*10);
    w=malloc(sizeof(float)*10);
    for(p1=v, p2=w; p1<v+n; p1++, p2++){ // p1 + 4octets et p2 + 4octets -> prend moins de place en mémoire
        pscal+= *p1 * *p2;
    }
    return pscal;
}

//Allocation dynamique -> besoin d'une variable temporaire (pointeur)
//exemple:polynome

void lagrange(int taille, double *p, double *x){

    double *v, *b;

    //matrice de dimension n+1 et vecteur de taille n
    v=(double *) malloc(sizeof(double)*(n+1)*(n+1)); //un seul vecteur
    b=(double *) malloc(sizeof(double)*(n+1));

    if (v==NULL && b==NULL){
        printf("Erreur");
        exit;
    }
    free(v);
}

//----------------------------------------------

//nb d'opérations pour l'addition de deux matrices: n²
//nb d'opérations pour le produit par un scalaire: n²
//nb d'opérations pour le produit matrice-vecteur: 2*n²
//nb d'opérations pour le produit matrice-matrice: 2*n^3


//2 déclarations possibles d'une matrice
// 1- float v[N][N]; (=tableau de tableaux)
// -> éléments accesibles par v[i][j]
// 2- float v[N*N]; (un seul vecteur)
// -> éléments accessibles par *(v+i*N+j)

//produit matrice-vecteur (par valeur)

void prodmatvec(float **a, float *x, float *res, int N){
    int i,j;
    for(i=0; i<N; i++){
        res[i]=0;
        for(j=0;j<N;j++){
            res[i]+= a[i][j]*x[j];
        }
    }
    return res;
}

//produit matrice-vecteur optimisé (par adresse)

void prodmatvec2(float *a, float *x, float *res, int N){
    float *p1, *p2, *p3;
    for(p1=a, p3=res; p3<res+N; p3++){
        *p3=0;
        for(p2=x; p2<x+N; p1++; p3++){ //p1++ me positionne à la ligne suivante
            *p3+=(*p1)*(*p2);
        }
    } return *p3;
}

//----------------------------------------------

//produit matrice à gauche de A et P
//permet de ne pas modifier la ligne i0 de A
//->calcul de la ligne i0 de PA: sum(p<i0,k> * a<k,j>)= a<i0,j>

//3 types de transformations :
// 1-multiplier à gauche par l'inverse -> on échange les lignes k et l
// 2-multiplier à gauche par lambda -> on multiplie la ligne i0 de A par lambda
// 3-multiplier à gauhe par la soustraction -> on soustrait la ligne l multipliée par lambda 
// à la ligne k de A

//----------------------------------------------

//ex 5

double horner(double *a, double x, int n)
{
  double y, *pa;
  y=*(a+n);
  
  for (pa=a+n-1; pa>=a; pa--){
      y= y*x + *pa;
  }

  return y;
}


int main(){
    int *v, *w;

    float pa= pscal_adresse(v,w);
    float pv= pscal_val(v,w);

    printf("pa= %f\n", pa);
    printf("pv= %f\n", pv);


    float **a = malloc(sizeof(float*));



}