public class TestSerre{
    public static void main(String[] args){
        Serre s1= new Serre(3);
        //Serre s2= new Serre(3);
        for(int i=0; i<3; i++){
            s1.planter();
        }

        double profitTotal=0;
        for(int i=0; i<2; i++){
            profitTotal+= s1.tab[i].estimer(2.90);
        }
        s1.planter();
    }
}