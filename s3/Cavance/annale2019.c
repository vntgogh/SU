int comparer_int(const void *i1, const void *i2) {
    const int *ii1=(const int *)i1;
    const int *ii2=(const int *)i2;
    return (*ii1<*ii2) - (*ii1>*ii2); //si renvoie -1, ii1>ii2, si renvoie 1, ii1<ii2, sinon ii1=ii2
}
int calcul_HIndex(PAuteur auteur, PABRAuteurs abr, PListeArticles
articles) {

    //cherche l'auteur dont la liste d'articles correspond à la liste d'articles articles
    PABRAuteurs abra=chercher_abr(auteur->nom, auteur->prenom, abr);

    if(abra!=NULL) {
        
        PListeArticles aut_articles=abra->articles; 
        assert(aut_articles!=NULL);

        //nombre d'articles dont on veut compter le nb de citations
        int nb_art=compter_articles(aut_articles);

        //crée la liste des nb de citations de articles
        int *art_citations=(int *)malloc(nb_art*sizeof(int));
        int i;
        for (i=0;i<nb_art; i++) {
            art_citations[i] = nb_citations(aut_articles->article,
            articles);
            aut_articles = aut_articles->suivant;
        }

        //trie dan sl'ordre décroissant la liste des nombres de citations de articles
        qsort(art_citations, nb_art, sizeof(int), comparer_int);

        for (i=0;i<nb_art;i++) {
            printf("nb citations: %d\n",art_citations[i]);
        }


        int hindex=0;
        for (i=0;i<nb_art; i++) {
            
            //récupère l'indice de l'article au plus petit nombre de citations supérieur à son indice+1
            if (art_citations[i]<i) {  
                hindex=i;
                break;
            }
        }

        free(art_citations);
        return hindex;
    }
    return 0;
}