

public class Coureur{
    private int numDossard;
    private double tempsAu100;
    private boolean possedeTemoin;
    
    public Coureur(int nd){
        this.numDossard=nd;
        this.tempsAu100=Math.random()*16;
        this.possedeTemoin=false;
    }
    public Coureur(){
        this((int)(Math.random()*1000)+1);
    }
    int getNumDossard(){
        return this.numDossard;
    }
    double getTempsAu100(){
        return this.tempsAu100;
    }
    boolean getPossedeTemoin(){
        return this.possedeTemoin;
    }
    public void setPossedeTemoin(boolean possedeTemoin){
        this.possedeTemoin=possedeTemoin;
    }
    public String toString(){
        String n;
        if (this.possedeTemoin){
            n="oui";
        }else{
            n="non";
        }
        String tpsAu100= String.format("%.2f", tempsAu100);
        return "Coureur : "+this.numDossard+" tempsAu100 : "+tpsAu100+" au 100m possedeTemoin : "+n;
    }
    public void passeTemoin(Coureur c){
        System.out.println("moi, coureur "+this.getNumDossard()+", je passe le temoin au coureur "+c.getNumDossard());
    }
    public void courir(){
        System.out.println("je suis le coureur "+this.numDossard+" et je cours");
    }
}