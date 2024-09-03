public class Joyau extends Contenu{
    private int nbpieces;

    public Joyau(String type,int quantite){
        super(type,quantite);
        this.nbpieces=(int)((Math.random()*5999)+1);
    }

    public int getnbpieces(){
        return super.getQuantite()*this.nbpieces;
    }

    public String toString(){
        return super.toString();
    }


}