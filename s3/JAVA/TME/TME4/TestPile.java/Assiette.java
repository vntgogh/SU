public class Assiette{
    private int diam;

    public Assiette(int d){
        this.diam=d;
    }

    public Assiette(){
        this(26);
    }

    public String toString(){
        return "Assiette de "+this.diam+" cm";
    }
}