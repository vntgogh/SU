public class Roue{
    private double diam;
    public Roue(double d){
        diam=d;
    }
    public Roue(){
        this(60);
    }
    public String toString(){
        return "Diametre : "+this.diam;
    }

    public double getDiam() {
        return this.diam;
    }

}