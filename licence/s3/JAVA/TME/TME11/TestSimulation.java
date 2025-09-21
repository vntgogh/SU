public class TestSimulation {
    public static void main(String [] args){
            Grille g=new Grille(10,10);
     
        try{
            Agent6 a=Agent6.getInstance(3,2,g);
            // Test du Singleton
            //Agent6 a2=Agent6.getInstance(3, 1, g);
            Simulation s=new Simulation(a,g, 15);
            s.lance(10);
        }
        catch(DeplacementIncorrectException e){
            System.out.println(e.getMessage());
            e.getCause();
        }
        catch(CoordonneesIncorrectesException e){
            System.out.println(e.getMessage());
            
        }
    
    }
}
