void compress_tab(int tab_brut[], int tab_compress[]) {
    int i =0;
    int j =0;
    while ( tab_brut[i] != -1){

        if (tab_brut[i] == tab_brut[i+1]){
            int cpt=1;
            tab_compress[j+1] = tab_brut[i];
            while (tab_brut[i]== tab_brut[i+1]){
                i++;
                cpt++;
            }
            tab_compress[j]=cpt;
            j=j+2;
        } else {
            tab_compress[j]= tab_brut[i];
            j++;
        }
        i++;
    }
    tab_compress[j] = -1;
}
