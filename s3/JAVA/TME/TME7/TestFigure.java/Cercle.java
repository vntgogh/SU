public class Cercle extends Ellipse{
    private double r;
    
    public Cercle(double rayon){
        super(rayon,rayon);
        this.r=rayon;
    }

    public double surface(){
        return super.surface();
    }

    public double perimetre(){
        return 2*PI*this.r;
    }
}