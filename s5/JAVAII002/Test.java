public class Test{
    public static void main(String[] args){

        Client c1 = new Client("yansi", "isnay");
        Client c2 = new Client("ines", "seni");
        Compte cp = new Compte(c1, -10000);
        Compte cp2 = new Compte(c2, 10000);
        Compte cp3 = cp;
        Agence a = new Agence("HarraouiCorp");
        a.addCompte(cp3);
        a.addCompte(cp2);

        // System.out.println(cp.toString());
        // System.out.println(cp2.toString());
        // System.out.println(cp3.toString());

        //System.out.println(cp.equals(cp3));
        
        System.out.println(a.toString());

    }
}