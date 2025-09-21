#include<stdint.h>
#include <stdlib.h>
#include <stdio.h>


/*Compléter la fonction C ci-dessous pour qu'elle renvoie le bit de position i de l'entier non signé n 
en utilisant uniquement des décalages et des opérateurs logiques.*/

unsigned int position(unsigned int n, unsigned int i)
{
    if (n&(1u<<i)){
        return 1;
    }
    return 0;
}

/*Compléter la fonction ci-dessous pour qu'elle compare deux entiers n et m non signés
 en utilisant uniquement des décalages et des opérateurs logiques et renvoie 1 si n>m et 0 sinon*/

int compare(uint16_t n, uint16_t m)
{
    int i = 15, b1, b2;
    do    
   { b1 = (n >> i) & 1; //bit de poids fort de n
     b2 = (m >> i) & 1; //bit de poids fort de m

        if (b1 != b2) {
            if (b1>b2){
                return 1;
            }else{
                return 0; 
            }
        }

        // si b1=b2 décaler et comparer les bits à la (i-1)ème position 
        i--;

    } while((b1 == b2) && ( i>=0  ));
    return 0;
    
}

/*Ecrire une fonction qui calcule qui retourne le PGCD de deux entiers {\it a} et {\it b} non signés
sur 16 bits en utilisant uniquement la soustraction comme opérateur algébrique.*/

uint16_t pgcd(uint16_t a, uint16_t b) {
    // Soustraction répétée jusqu'à ce que a et b soient égaux
    while (b != 0) {
        if (a >= b) { // Assurer que a est le plus grand des deux
            a -= b;
        }
        // Échanger a et b si nécessaire
        uint16_t t = a;
        a = b;
        b = t;
    }
    return a;
}


//Euclide
void euclide(uint16_t a, uint16_t b){
    int u1=1, u2=0, u3=a;
    int v1=0, v2=1, v3=b;
    int t1,t2,t3;
    while(v3!=0){
        int q=u3/v3;
        t1= u1-q*v1;
        t2= u2-q*v2;
        t3= u3-q*v3;
        
        u1=v1;
        u2=v2;
        u3=v3;
        v1=t1;
        v2=t2;
        v3=t3;
    }printf("D'après le théorème d'Euclide, les coefficients sont u1= %d, u2= %d et vérifient %d*%d+%d*%d = %d\n", u1,u2,u1,a,u2,b,u3);
}

int main(){
    int32_t

    printf("%d\n", pgcd(264,198));
    euclide(391,276);
}