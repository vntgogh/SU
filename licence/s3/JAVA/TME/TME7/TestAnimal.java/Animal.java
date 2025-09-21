public abstract class Animal{
    protected int a;
    protected String n;

    public Animal(String name){
        this.n=name;
        this.a=1;
    }
    
    public Animal (int age, String name){
        this(name);
        this.a=age;
    }

    public String toString(){
        if(this.a==1){
            return this.n+ ", "+this.a+ " an";
        }
        return this.n+ ", "+this.a+ " ans";
    }

    public void vieillir(){
        this.a+=1;
        System.out.println(this.n+" a gg 1 an!");
    }

    public abstract String crier();

}