public class Legume{
    protected double poids;
    private static int cpt=0;
    public final int id;

    public Legume(double p){
        poids=p;
        id=cpt;
        cpt++;
    }

    public String toString(){
        return "id : "+id+" poids : "+poids+" kg";
    }

    public double estimer(double prixParKilo){
        return poids*prixParKilo;
    } 
        
}