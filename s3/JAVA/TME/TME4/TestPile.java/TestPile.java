public class TestPile{
    public static void main(String[] args){
        Assiette a1 = new Assiette(30);
        Assiette a2 = new Assiette();
        Assiette a3 = new Assiette(14);
        Assiette a4 = new Assiette();

        System.out.println(a1.toString());
        System.out.println(a2.toString());
        System.out.println(a3.toString());

        int tMax = 3;
        Pile p1 = new Pile(tMax);

        System.out.println(p1.toString());
        System.out.println("Pile vide?"+p1.estVide());
        System.out.println("Pile remplie?"+p1.estPleine());

        p1.empiler(a1);
        p1.empiler(a2);
        p1.empiler(a3);

        System.out.println(p1.toString());
        System.out.println("Pile vide? "+p1.estVide());
        System.out.println("Pile remplie? "+p1.estPleine());

        p1.depiler();
        System.out.println(p1.toString());

        System.out.println(p1.toString());
        System.out.println("Pile vide? "+p1.estVide());
        System.out.println("Pile remplie? "+p1.estPleine());

        p1.empiler(a3);
        p1.empiler(a4);

        System.out.println(p1.toString());
        System.out.println("Pile vide? "+p1.estVide());
        System.out.println("Pile remplie? "+p1.estPleine());

        for(int j=0; j<4; j++){
            p1.depiler();
        }
        System.out.println(p1.toString());
        System.out.println("Pile vide? "+p1.estVide());
        System.out.println("Pile remplie? "+p1.estPleine());
    }
}