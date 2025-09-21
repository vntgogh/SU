public class Presentation{
    public static void main(String[] args){
        Personne pi= new Personne("Pierre", 25);
        Personne pa= new Personne("Paul", 37);
        for(int i =0; i<20; i++){
            pi.vieillir();
        }int j=0;
        while(j<10){
            j++;
            pa.vieillir();
        }
        System.out.println(pi.toString());
        pa.sePresenter();
    }
}