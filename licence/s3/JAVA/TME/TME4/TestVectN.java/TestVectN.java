public class TestVectN{
    public static void main(String[] args){
        VectN v1 = new VectN(4, 10);
        VectN v2 = new VectN();
        VectN v3 = new VectN(4, 5, 6);

        System.out.println(v1.toString());
        System.out.println(v2.toString());
        System.out.println(v3.toString());

        System.out.println("\n");

        System.out.println("Somme des éléments de v1 : "+v1.somme());
        System.out.println("Somme des éléments de v2 : "+v2.somme());
        System.out.println("Somme des éléments de v3 : "+v3.somme());

        System.out.println("\n");

        int [] tab2 = v3.getTabCopie();        
        tab2[0] = 100; // modifie tab2 -> Copie des éléments de v3
        System.out.println("v3 = "+v3);

        System.out.println("\n");
        
        int [] tab1 = v3.getTab(); 
        tab1[0] = 100; // modifie v3 -> Copie de la référence de v3
        System.out.println("v3 = "+v3);        
    }
}

// question 27.4
/* Ajouter un accesseur getTab() qui renvoie directement le tableau n'est pas une bonne idée,
car cela permet aux utilisateurs de la classe de modifier le tableau et la sécurité des données n'est plus assurée. */
