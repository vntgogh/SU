public class Test{
    public static void main(String[] args){
        Station s1= new Station("Alpha");
        Generateur g1= new Generateur("Générateur",30);
        Generateur g2= new Generateur("Grand Générateur",100);

        s1.Construire(g1);
        s1.Construire(g2);
        for(int i=0; i<3; i++){
            s1.Construire(new Usine("Usine", 25));
        }

        s1.phaseAlimentation();
        s1.phaseProduction();
        
    }
}