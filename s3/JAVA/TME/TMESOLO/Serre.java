public class Serre{
    public Legume[] tab;
    private static int plante=0;
    private final int m;

    public Serre(int max){
        tab= new Legume[max];
        m=max;
    }

    public boolean estPleine(){
        if(m < plante){
            return true;
        }
        return false;
    }

    public void planter(){
        if(this.estPleine()==false){
            if((double)(Math.random()*(1)) > 0.6){
                tab[plante]=new Oignon((double)(Math.random()*(100)),(char)(Math.random()*(1)));
                System.out.println("Un oignon est planté dans la serre");
            }else{
                tab[plante]=new Laitue((double)(Math.random()*(100)), (double)(Math.random()*(2)));
                System.out.println("Une laitue est plantée dans la serre");
            }
            plante++;
        }else{
            System.out.println("Plus de place dans la serre !");
        }
    }
    
}