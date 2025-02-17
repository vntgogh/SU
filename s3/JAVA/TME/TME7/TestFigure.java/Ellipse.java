public class Ellipse extends Figure2D{
    private double a, b;
    protected static final double PI= Math.PI;

    public Ellipse(double a, double b){
        this.a=a;
        this.b=b;
    }

    public double surface(){
        return PI*a*b;
    }

    public double perimetre(){
        return 2*PI*Math.sqrt(((a*a)+(b*b))/2);
    }
}