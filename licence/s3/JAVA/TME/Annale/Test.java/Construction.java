public class Construction{
    private String nom;
    private double cout;
    private static int cpt=0;
    private final int id;

    protected Construction(String n, int c){
        nom=n;
        cout=c;
        id=cpt;
        cpt++;
    }

    public double getCout(){
        return cout;
    }
    public String toString(){
        return "["+id+"] "+nom;
    }
}