public class Triangle{

    private Point p1, p2, p3;

    public Triangle(Point pt1, Point pt2, Point pt3){
        this.p1=pt1;
        this.p2=pt2;
        this.p3=pt3;
    }
    
    public Triangle(){
        this(new Point(), new Point(), new Point());
    }

    public Triangle(Triangle tr){
        this.p1=new Point(tr.p1.getX(), tr.p1.getY());
        this.p2=new Point(tr.p2.getX(), tr.p2.getY());
        this.p3=new Point(tr.p3.getX(), tr.p3.getY());
    }
    
    public String toString(){
        return "{"+p1.toString() +", "+ p2.toString() + ", "+ p3.toString()+"} ";
    }

    public double getPerimetre(){
        double p=p1.distance(p2)+p2.distance(p3)+p3.distance(p1);
        return p;
    }
    
}