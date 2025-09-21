public class EnsembleFeuilles extends Legume{
    private double degGivre;

    public EnsembleFeuilles(double p, double d){
        super(p);
        degGivre=d;
    }
    
    public double estimer(double prixParKilo){
        return (1-degGivre)*poids*prixParKilo;
    }

    public String toString(){
        return super.toString()+" degré de givre : "+degGivre+" %";
    }

}