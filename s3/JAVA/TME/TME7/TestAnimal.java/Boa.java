public class Boa extends Animal{
    private static final int nbp=0;

    public Boa(int age, String name){
        super(age,name);
    }
    public Boa(String name){
        super(name);
    }

    public String toString(){
        return super.toString()+" de type Boa "+nbp+ " patte";
    }

    public String crier(){
        return " fait pst";
    }
}