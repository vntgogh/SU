public abstract class Module extends Construction{
    protected int production;

    public Module(String n, int c, int p){
        super(n, c);
        production=p;
    }
    
    public abstract void produire(Station s);
}