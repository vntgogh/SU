/*Nous vous rappelons les tarifs pour la visite de la Tour de Londres si vous achetez les billets en ligne
 (tarifs du 12 juin 2018) :

    adulte : 22,7 £
    enfant (entre 5 et 15 ans) : 10,75 £
    enfant de moins de 5 ans : gratuit
    famille (2 adultes et 3 enfants au maximum) : 57,80

Nous souhaitons maintenant appliquer le tarif famille autant de fois que possible. 
Dans le programme suivant complétez la fonction prixEntree qui prend en paramètre le nombre d'adultes 
et d'enfants de plus de cinq ans et qui renvoie la somme à payer. Les personnes non comprises dans 
les entrées famille paient en fonction de leur âge.

Le tarif proposé doit bien sûr être le plus intéressant pour les visiteurs.*/

#include <stdio.h>
#include <math.h>

float prixEntree( int nbad, int nben){
    float pnorm= nbad*22.7 + nben*10.75;
    float ptarif=0.0;
    while(nbad >=2 && nben>=3){
        ptarif+= 57.8;
        nbad-=2;
        nben-=3;
    }ptarif+= nbad*22.7 +nben*10.75;
    return fmin(pnorm, ptarif);
}

int main(){
    int nbad =0;
    int nben=4;
    float p= prixEntree(nbad,nben);
    printf("%d adulte(s), %d enfant(s) = %.2f livres\n",nbad,nben,p);
    return 0; 
}