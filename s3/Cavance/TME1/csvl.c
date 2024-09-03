#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int compte_mots_chaine(char *chaine) {
    int cpt=0, i=0;
    while(chaine[i]!= '\0'){
        if(chaine[i]== ' '){
            cpt++;
        }
        i++;
    }cpt++;
    return cpt;
}

char **decompose_chaine(char *chaine)
{

  /* Fonction vue en TD, exercice 2, question 7 */

  char *pc= chaine;
  int nb_mots=0; // longueur du tableau 
  char **ptab; //tableau où vont etre copiés chaque mot de la chaine
  char *psrc_mot; 
  int ind_mot=0; //indice des éléments du tableau

  //comptages des mots
  nb_mots=compte_mots_chaine(chaine);
	
  if (nb_mots == 0)
    return NULL;
  // allocation du tableau
  ptab = malloc((nb_mots + 1) * sizeof(char *));
  ptab[nb_mots] = NULL;
	
  // copie des mots
	  pc=chaine;
  while (*pc)
    {
      if(*pc == ' ')
        {
          pc++;
          continue;
        }

      psrc_mot = pc;

      while((*pc != ' ') && (*pc)){
        pc++;
      }
      //allocation du mot
      ptab[ind_mot] = malloc((pc - psrc_mot + 1)* sizeof(char));
      //copie du mot
      memcpy(ptab[ind_mot], psrc_mot, pc - psrc_mot); //copie de ptab[ind_mot] dans psrc_mot et initialisation de (pc-prsc_mot) caractères
      //insertion du marqueur de fin de chaine
      *(ptab[ind_mot] + (pc - psrc_mot)) = '\0';

      ind_mot++;
    }
  return ptab;
}

int compte_mots(char **ptab_mots)
{
  int cpt=0;
  while(ptab_mots[cpt]){
    cpt++;
  }
  return cpt;
}

char *compose_chaine(char **ptab_mots){
	if (!ptab_mots) {return NULL;}
	
	//Calcule le nombre de caractère dans la chaine res.
	
	int cpt = 0, cpt_c = 0;
	int nb_carac = compte_mots(ptab_mots);  //Cela permet de compter le nombre d'espace de la chaine (+ 1 pour le '\0').
	while (ptab_mots[cpt]){
		while (ptab_mots[cpt][cpt_c] != '\0'){
			nb_carac++;
			cpt_c++;
		}
		cpt++;
		cpt_c = 0;
	}
	
	char *res = (char*) malloc(sizeof(char) * (nb_carac));
	cpt = 0;
	cpt_c = 0;
	
	//On place chaque caractère des mots dans la chaine res.
	
	int ind_char = 0;
	while (ptab_mots[cpt]){
		while (ptab_mots[cpt][cpt_c] != '\0'){
			res[ind_char] = ptab_mots[cpt][cpt_c];
			ind_char++; cpt_c++;
		}
		res[ind_char] = ' ';
		ind_char++; cpt++;
		cpt_c = 0;
	}
	
	res[ind_char-1] = '\0';
	return res;
}
		
void detruit_tab_mots(char **ptab_mots)
{
  /* Fonction vue en TD, exercice 2, question 5 */

  int i=0;
  if (ptab_mots)
    while(ptab_mots[i])
      free(ptab_mots[i++]);
  free(ptab_mots);
}

void affiche_tab_mots(char **ptab_mots)
{
  for(int j=0; j<compte_mots(ptab_mots);j++){
        printf("%s", ptab_mots[j]);
        printf(" ");
  }
  printf("\n");
}

char **reduit_tab_mots(char **ptab_mots)
{
  /* a completer exercice 4, question 1 */
}

int main() {

  //exercice 3, question 3
  char *ta[6]={"raze", "et","omen","supremacy","periodt",NULL};
  affiche_tab_mots(ta);
  
  int c0= compte_mots(ta);
  printf("contient %d mots\n", c0);


  char *chaine=compose_chaine(ta);
  printf("Phrase recomposée : %s\n", chaine);
   //exercice 3, question 5 
   //exercice 4, question 1

  return 1;
}
