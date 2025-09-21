public class ChampiToxic extends Champignon implements Toxic{

    public ChampiToxic(String name){
        super(name);
    }
    public double getPoids(){
        return super.getPoids();
    }
    public boolean estToxic(){
        return true;
    }
}