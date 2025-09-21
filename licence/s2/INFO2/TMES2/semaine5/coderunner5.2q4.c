int compare_tab(int tab1[], int tab2[]) {
    int i=0;
    while ( (tab1[i] != -1) && (tab2[i] != -1)){
        if ( tab1[i] != tab2[i]){
          return -1;
        }
        i++;
    }
    if (tab1[i] == tab2[i]){
        return 0;
    } else {
        return -1;
    }
}
