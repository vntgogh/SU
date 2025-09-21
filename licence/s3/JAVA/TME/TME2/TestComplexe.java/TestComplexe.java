public class TestComplexe{
    public static void main(String [] args){
        Complexe c1= new Complexe(1,1);
        Complexe c2= new Complexe(2,2);
        Complexe c3= new Complexe(0,1);
        System.out.println(c1.toString());
        System.out.println(c2.toString());
        System.out.println(c3.toString());

        c1.estReel();
        c2.estReel();
        c3.estReel();

        Complexe c1pc3= c1.addition(c3);
        System.out.println("L'addition de "+c1.toString()+" et "+c3.toString()+" est "+c1pc3.toString());
        Complexe c2pc3= c2.addition(c3);
        System.out.println("L'addition de "+c2.toString()+" et "+c3.toString()+" est "+c2pc3.toString());
        Complexe c1c2=c1.multiplication(c2); 
        System.out.println("Le produit de "+c1.toString()+" et "+c2.toString()+" est "+c1c2.toString());
        Complexe c3c3= c3.multiplication(c3);
        System.out.println("Le produit de "+c3.toString()+" au carre est "+c3c3.toString());

    
    }
}