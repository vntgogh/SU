public class TestPersonne{
    public static void main(String[] args){
        Personne p1= new Personne();
        Personne p2= new Personne();
        Personne p3= new Personne();
        System.out.println(p1.toString());

        p1.epouser(p2);
        p1.epouser(p3); //impossible
        p3.epouser(p1);

        System.out.println(p1.toString());
        System.out.println(p2.toString());
        System.out.println(p3.toString());

        p1.divorcer();
        p3.divorcer();

        System.out.println(p1.toString());
        System.out.println(p2.toString());
        System.out.println(p3.toString());
    }
}