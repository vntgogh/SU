public class TestAnimal{
    public static void main(String[] args){
        Vache a1= new Vache(3,"Mu");
        Vache a2= new Vache(10,"Mo");
        Vache a3= new Vache("Mew");

        Boa a4= new Boa(4, "Bouh");
        Boa a5= new Boa("Bahh");

        /*System.out.println(a1.toString());
        System.out.println(a2.toString());
        System.out.println(a3.toString());
        System.out.println(a4.toString());
        System.out.println(a5.toString());*/

        a4.vieillir();
        System.out.println(a4.toString());

        Menagerie m1= new Menagerie(4);
        System.out.println(m1.toString()); // Ménagerie vide

        m1.ajouter(a5);
        m1.ajouter(a4);
        m1.ajouter(a3);
        m1.ajouter(a2);
        System.out.println(m1.toString());

        m1.ajouter(a1); // pas assez de place

        m1.vieillirTous();
        System.out.println("\n"+m1.toString());

        m1.midi();




        
    }
}