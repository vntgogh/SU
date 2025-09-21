public class Gardien extends Contenu{
    private int pdv=(int)(Math.random()*201);
    private static String[] tabtype=new String[]{"Zombie","Squelette","Creeper","Araignée"};
    /*Faire un attribut ArrayList/tableau qui va contenir les type de Gardien
    Ensuite faire une variable random entre 0 et le size pour selectionne un type de Gardien au hasard
     */
    public Gardien(int quantite){
        
        super(tabtype[(int)(Math.random()*4)],quantite);
    }

    public Gardien(String type,int quantite){
        super(type,quantite);
    }

    public Gardien(Gardien ga){
        this(ga.type+"Cloné",ga.getQuantite());
        this.pdv=ga.getPdv();
    }

    public void pertePV(int n){
        this.pdv-=n;
    }
    

    public int getPdv(){
        return this.pdv;
    }

    public String toString(){
        return super.toString()+" a "+this.pdv+" PV ";
    }
    
    
}