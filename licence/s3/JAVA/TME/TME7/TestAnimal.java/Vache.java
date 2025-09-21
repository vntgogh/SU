public class Vache extends Animal{
    private double ql;
    private static final int nbp=4;

    public Vache(int age, String name){
        super(age, name);
        this.ql=Math.random()*(25)+5;
    }

    public Vache(String name){
        this(1,name);
    }
    
    public String toString(){
        return super.toString()+" de type Vache "+nbp+ " pattes";
    }

    public String crier(){
        return " fait meuh";
    }
}