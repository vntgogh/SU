public class TestProjet {
    public static void main(String[]args){
        System.out.println("Nombre de personnes : "+Personne.getNbPers());

        /*Personne p1= new Personne();
        Personne p2= new Personne();

        System.out.println(p1.toString());
        System.out.println(p2.toString());
        System.out.println("Nombre de personnes : "+Personne.getNbPers());*/

        System.out.println("Nombre de trios : "+Trio.getCompt());

        Projet pr1 = new Projet("P3X-774");
        Projet pr2 = new Projet("P3X-775");
        Projet pr3 = new Projet();
        System.out.println(pr1.toString());
        System.out.println(pr2.toString());
        System.out.println(pr3.toString());

        System.out.println("Nombre de projet :"+Projet.getNbProjet());
        System.out.println("Nombre de personnes : "+Personne.getNbPers());
        System.out.println("Nombre de trios : "+Trio.getCompt());
    }
}