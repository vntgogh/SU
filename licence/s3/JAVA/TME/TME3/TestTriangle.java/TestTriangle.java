public class TestTriangle{
    public static void main(String [] args){
        Point p1= new Point(1,2);
        Point p2= new Point();
        Point p3= new Point(1,2);
        Point p4=p1;

        System.out.println(p1.equals(p2)); // false
        System.out.println(p1.equals(p3)); // true
        System.out.println(p1.equals(p4)); // true

        double d=p1.distance(p2);
        String dist= String.format("%.2f",d);
        System.out.println("Distance between "+p1.toString()+" and "+p2.toString()+" : "+dist);

        Triangle t1=new Triangle(p1,p2,p3);
        double t=t1.getPerimetre();
        String tp= String.format("%.2f",t);
        System.out.println("Coordonnees de t1 : "+t1.toString());
        System.out.println("Perimetre du triangle "+t1.toString()+ ": "+tp);

        Triangle t2= new Triangle(t1); // exercice 20 question 6
        Triangle t3=t1;
        
        System.out.println(t1.equals(t2)); // false
        System.out.println(t1.equals(t3)); // true

        p1.deplaceToi(2.5, 1.);
        System.out.println("Coordonnees de t2 : "+t2.toString()); //le point p1 de t2 n'a pas bougé
        System.out.println("Coordonnees de t1 : "+t1.toString()); //le point p1 de t1 a bien été modifié
    }
}