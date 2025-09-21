public class Usine extends Module implements Alimentable{
    private int consommation;
    private boolean actif;

    public Usine(String n, int p){
        super(n,10,p);
        consommation=2*p;
        actif=false;
    }

    public void produire(Station s){
        if(actif==true){
            s.materiaux+=(consommation/2);
            System.out.println(super.toString()+" produit "+(consommation/2)+" d'énergie");
        }else{
            System.out.println(super.toString()+" inactive: pas de production");

        }
    }
    
    public void alimenter(Station s){
        if(s.energie>0){
            actif=true;
            s.addEnergie(-consommation);
            System.out.println(s.toString()+" alimentée");
        }else{
            actif=false;
        }
    }
}