public class Generateur extends Module{
    private int production;

    public Generateur(String n, int p){
        super(n,p/2,p);
        production=p;
    }
    
    public void produire(Station s){
        s.addEnergie(production);
        System.out.println(super.toString()+" produit "+production+" d'énergie");
    }
}