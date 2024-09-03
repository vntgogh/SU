//import java.util.ArrayList;

public class TestForet{
    public static void main(String[] args){
        
        Foret f1= new Foret(10);

        for (int i = 0; i < 10; i++) {
            if (Math.random() < 0.3) {
                f1.placer(new Arbre("Pin"));
            } else {
                f1.placer(new Champignon("Cèpe"));
            }
        }

        for (int j=0; j<3; j++){
            f1.placer(new ChampiToxic("Amanite"));
        }

        // System.out.println(f1.toString());

        // ArrayList<Champignon> lc= f1.ramasserChampignons();
        // System.out.println(f1.toString());

        // ArrayList<Ramass> lt= f1.ramasserTout();
        // System.out.println(f1.toString());

        Panier p1= new Panier(8.0);
        
        // p1.add(new ChampiToxic("amanite"));
        // p1.add(new Champignon("Cèpe"));
        // System.out.println(p1.getPoids());
        // System.out.println(p1.toString());
        f1.ramasser(p1);
        System.out.println(p1.toString());
        System.out.println(f1.toString());

    }
}