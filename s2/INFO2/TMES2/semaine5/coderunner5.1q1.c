int compte_mots(char *ch) {
   int cpt=0;
   int i=0;
   while (*(ch+i) != '\0') {
      while (*(ch+i) != ' ' && *(ch+i+1) == ' '){
          i++;
          cpt++;
      }

      if (*(ch+i) != ' ' && *(ch+i+1) == '\0'){
        cpt++;
      }

      i++;
   }
   return cpt;
}
