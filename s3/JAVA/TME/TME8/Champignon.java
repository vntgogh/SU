public class Champignon implements Ramass{
    protected String nom;
    private double poids;

    public Champignon(String n){
        poids=(float)Math.random()*(4);
        nom=n;
    }

    public double getPoids(){
        return poids;
    }

    public String toString(){
        return nom+" "+poids+" kg";
    }
}