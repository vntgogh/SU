public class Rectangle extends Figure2D{
    private double lo, la;

    public Rectangle(double larg,double log){
        this.lo=log;
        this.la=larg;
    }

    public double surface(){
        return this.lo*this.la;
    }

    public double perimetre(){
        return (2*this.lo)+(2*this.la);
    }
}