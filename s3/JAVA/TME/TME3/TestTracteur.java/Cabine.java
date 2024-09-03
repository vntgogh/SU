public class Cabine{
    private double vol;
    private String coul;
    public Cabine(double v, String c){
        vol=v;
        coul=c;
    }
    public String toString(){
        return ("Volume : "+this.vol+", Couleur : "+ this.coul);
    }
    public void setCouleur(String couleur){
        this.coul=couleur;
    }

    public double getVol() {
        return this.vol;
    }

    public String getCoul() {
        return this.coul;
    }


}