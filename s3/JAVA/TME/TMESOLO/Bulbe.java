public class Bulbe extends Legume{
    private char maladie;

    public Bulbe(double p, char m){
        super(p);
        maladie=m;
    }

    public String toString(){
        return super.toString()+" maladie : "+maladie;
    }

    public double facteurMaladie(char maladie){
        return 1- 0.18 * (maladie- 'A');
    }

    public double estimer(double prixParKilo){
        return this.facteurMaladie(maladie)*poids*prixParKilo;
    }
}