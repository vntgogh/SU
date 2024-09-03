int est_incluse(char ch1[], char ch2[]) {
    if (ch2[0] == '\0' ){
        return 0;
    } else{
        if (est_deb(ch1,ch2) == 1){
            return 1;
        } else {
            return est_incluse(ch1,ch2+1);
       }
    }
    return 0;
}
