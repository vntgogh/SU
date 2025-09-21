public class Tracteur{
    private Cabine ca;
    private Roue roue1, roue2, roue3, roue4;
    public Tracteur(Cabine cab, Roue ro1, Roue ro2, Roue ro3, Roue ro4){
        this.ca= cab;
        this.roue1= ro1;
        this.roue2= ro2;
        this.roue3= ro3;
        this.roue4= ro4;
    }
    public Tracteur(Tracteur tr2){
        this.ca= new Cabine(tr2.ca.getVol(),tr2.ca.getCoul());
        this.roue1= new Roue(tr2.roue1.getDiam());
        this.roue2= new Roue(tr2.roue2.getDiam());
        this.roue3= new Roue(tr2.roue3.getDiam());
        this.roue4= new Roue(tr2.roue4.getDiam());
    }
    public String toString(){
        return ("Cabine : ("+ca.toString()+"), Roues : 1 -> "+this.roue1+", 2 -> "+this.roue2+", 3 -> "+this.roue3+", 4 ->"+this.roue4);
    }
}