public class Cone{
    private static double PI=3.14159;
    private double r,h;
    private static int nbCones;

    public Cone(double rayon, double hauteur){
        this.r=rayon;
        this.h=hauteur;
        nbCones++;
    }

    public Cone(){
        this(Math.random()*10, Math.random()*10);
    }

    public double getVolume(){
        return (1.0/3.0)*PI*this.h*this.r*this.r;
    }

    public String toString(){
        return String.format("Cone r= %.2f, h= %.2f, V= %.6f",this.r,this.h,this.getVolume());
    }

    public static int getNbCones(){
        return nbCones;
    }
}