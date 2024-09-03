#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void min_max_moy(int *tab, int taille, int *min, int *max, float *moy){ //exercice 1
    *min = tab[0];
    *max = tab[0];
    int som = 0;
    for (int i=0; i<taille; i++){
        if (*min<tab[i]){
            *min = tab[i];
        }
        if (*max>tab[i]){
            *max = tab[i];
        }
        som += tab[i];
    } 
    *moy= (float)som/ (float) taille;
}

void min_max_som(int *t, int tai, int *min, int *max,float *som){
    if (tai<2){
        *min=t[0];
        *max=t[0];
        *som=t[0];
    }else{
        if(t[0]< *min){
            *min=t[0];
        }if(t[0]> *max){
            *max=t[0];
        }
        *som+=t[0];
        min_max_som(t+1,tai-1,min,max,som);
    }
}


//char *chaine=malloc(sizeof(char)*(nb_mots+1)); +1 pour le dernier mot qui n'est pas suivi d'espace 
int compte_mots_chaine(char *chaine){ //exercice 2 question 4
    int cpt=0, i=0;
    while(chaine[i]!= '\0'){
        if(chaine[i]== ' '){
            cpt++;
        }
        i++;
    }cpt++;
    return cpt;
}

int compte_mots(char **tab_chaine){
    int cpt=0, i=0,j=0;
    while (tab_chaine[i]){
        cpt+= compte_mots_chaine(tab_chaine[i]);
        i++;
    } return cpt;
}

void detruit_tabchaine(char **tab_chaine){
    int i=0;
    if(tab_chaine){
        while(tab_chaine[i]){
            free(tab_chaine[i]);
            i++;
        }
        free(tab_chaine);
    }
}

char **decompose_chaine(char *chaine){
    int i=compte_mots_chaine(chaine);
    char **tab_chaine=malloc(sizeof(char *)*(i+1));
    if(i==0){ return NULL;}
    char *tok=strtok(chaine, " ");
    for (int j=0; j<i;j++){ 
            strcpy(tab_chaine[j], tok); // copie chaque mot de chaine dans chaque élément de tab_chaine
            free(tok);
    }
    return tab_chaine;
}

int main(){
    
    int mii,maa;
    float moo;
    /*for (int n=1;n<101;n++){
        int *t0=(int *)malloc(n*sizeof(int));
        for (int k=0; k<n; k++){
            t0[k]= k;
        }
        //min_max_moy(t0,n,&mii,&maa,&moo);
        min_max_som(t0,n,&mii,&maa,&moo);
        printf("Maximum : %d\n", maa);
        printf("Minimum : %d\n", mii);
        printf("Moyenne : %.2f\n", moo/(float)n);
        free(t0);        
    }*/

    char *ch  = "i am lost";
    printf("%s contient %d mots\n",ch, compte_mots_chaine(ch));

    char **ta=malloc(sizeof(char)*3);
    *ta="raze et";
    *(ta+1)=" omen supremacy ";
    *(ta+2)="periodt";
    for(int j=0; j<3;j++){
        printf("%s", ta[j]);
    }

    int cpt0=compte_mots(ta);
    for (int n=0; n<cpt0; n++){
        printf("%s contient %d mots\n", *(ta+n), cpt0);
    }    
    
    /*char **dcp=decompose_chaine(ch);
    if (dcp) {
        for (int i = 0; dcp[i] != NULL; i++) {
            printf("Mot %d : %s\n", i + 1, dcp[i]);
            free(dcp[i]);
        }
        free(dcp);
    } else {
        printf("Aucun mot trouvé dans la chaîne.\n");
    }*/
    detruit_tabchaine(ta);
    free(ch);
    return 0;
}