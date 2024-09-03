public class TestFigure{
    public static void main(String[] args){
        Rectangle r1 = new Rectangle(2,3);
        Carre ca1 = new Carre(2);

        Ellipse e1 = new Ellipse(1,1);
        Cercle c1 = new Cercle(1);

        System.out.println("Surface rectangle : "+r1.surface());
        System.out.println("Périmètre rectangle : "+r1.perimetre());

        System.out.println("Surface carré : "+ca1.surface());
        System.out.println("Périmètre carré : "+ca1.perimetre());

        System.out.println("Surface ellipse : "+e1.surface());
        System.out.println("Périmètre ellipse : "+e1.perimetre());

        System.out.println("Surface cercle : "+c1.surface()); //doit etre égale à la surface de e1
        System.out.println("Périmètre cercle : "+c1.perimetre()); //doit etre égal au perimetre de e1

    }
}