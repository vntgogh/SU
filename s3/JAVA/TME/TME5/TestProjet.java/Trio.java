public class Trio {
    private static int compteur=0;
    private int numero;
    private Personne[] tp;

    public Trio(){
        compteur++;
        this.tp = new Personne[3];
        for (int i=0; i<3; i++){
            this.tp[i]= new Personne();
        }
        this.numero=compteur;
    }
    
    public String toString(){
        return "Trio "+this.numero+" : "+tp[0].toString()+", "+tp[1].toString()+", "+tp[2].toString();
    }
    
    public static int getCompt(){
        return compteur;
    }
}
