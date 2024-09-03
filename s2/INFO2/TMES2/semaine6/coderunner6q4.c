int est_deb(char ch1[], char ch2[]){
    if(ch1[0] != '\0'){
      if (ch1[0] == ch2[0]){
        return est_deb(ch1+1,ch2+1);
      } else if (ch1[0] != ch2[0] ) {
        return 0;
      }
    }else{
        return 1;
    }
    return 0;
}
