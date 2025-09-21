public class Point {
    private double x;
    private double y;

    public Point(double posx, double posy){
        this.x=posx;
        this.y=posy;
    }

    public Point(){
        this(Math.random()*10,Math.random()*10);
    }
    
    public String toString(){
        String px= String.format("%.2f",this.x);
        String py= String.format("%.2f",this.y);
        return "("+px+ ", "+py+")";
    }
    
    public double distance(Point p){
        return Math.sqrt(((this.x-p.x)*(this.x-p.x))+((this.y-p.y)*(this.y-p.y)));
    }
    
    public void deplaceToi(double newx, double newy){
        this.x=newx;
        this.y=newy;
    }

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public boolean equals(Point tr2){
        Point p= tr2 ;
        return ( this.x==p.x ) && (this.y==p.y);            
    }

}