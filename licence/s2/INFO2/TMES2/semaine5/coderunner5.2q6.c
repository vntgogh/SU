void decompress_tab(int tab_brut[], int tab_compress[]) {
    int i =0;
    int j =0;
    while ( tab_compress[i] != -1){
        if (tab_compress[i] != 0 && tab_compress[i] != 1){
            for (int k = 0; k<tab_compress[i]; k++){
                tab_brut[j]= tab_compress[i+1];
                j++;
            }
            i=i+2;

        } else {
            tab_brut[j] = tab_compress[i];
            j++;
            i++;
        }
    }
    tab_brut[j] = -1;
}
