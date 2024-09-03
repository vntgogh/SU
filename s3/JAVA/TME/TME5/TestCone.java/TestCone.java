public class TestCone{
    public static void main(String[] args){
        System.out.println("Nombre de cones :"+Cone.getNbCones());

        Cone c1= new Cone(12,1.2);
        Cone c2= new Cone();

        System.out.println(c1.toString());
        System.out.println(c2.toString());

        System.out.println("Nombre de cones :"+ Cone.getNbCones());
    }
}