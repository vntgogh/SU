public class TestTracteur{
    public static void main (String[] args){
        Roue r1= new Roue(120);
        Roue r2= new Roue(120);
        Roue r3= new Roue();
        Roue r4= new Roue();
        Cabine c1 = new Cabine(3, "bleue");
        Tracteur t1= new Tracteur(c1, r1, r2, r3, r4);
        System.out.println(t1.toString());

        Tracteur t2= new Tracteur(t1);
        c1.setCouleur("rouge");
        
        System.out.println(t1.toString());
        System.out.println(t2.toString());
    }
}