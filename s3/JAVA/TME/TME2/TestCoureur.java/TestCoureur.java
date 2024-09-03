public class TestCoureur{
    public static void main(String  [] args){
        Coureur c1= new Coureur();
        Coureur c2= new Coureur();
        Coureur c3= new Coureur();
        Coureur c4= new Coureur();
        double tpstot=0.;
        c1.courir();
        c1.passeTemoin(c2);
        tpstot+=c1.getTempsAu100();
        c2.courir();
        c2.passeTemoin(c3);
        tpstot+=c2.getTempsAu100();
        c3.courir();
        c3.passeTemoin(c4);
        tpstot+=c3.getTempsAu100();
        c4.courir();
        tpstot+=c4.getTempsAu100();
        System.out.println("Le temps total mis par les coureurs pour le 400m est "+tpstot+".");
    }
}