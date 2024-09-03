import java.util.ArrayList;

public class Agence {
    private String nom;
    private ArrayList<Compte> l;

    public Agence(String n){
        this.nom=n;
        this.l = new ArrayList<>();
    }

    public void addCompte(Compte c){
        for(int i=0; i<this.l.size(); i++){
            if (l.get(i).equals(c)){
                return;
            }
        }
        l.add(c);
    }

    public String toString() {
        String s = "Agence "+nom+" :\n";
        for(int i=0 ; i<l.size();i++){
            s += l.get(i).toString()+"\n";
        }
        return s;
    }

    public ArrayList<Compte> getComptesFor(Client c){
        ArrayList<Compte> cc = new ArrayList<Compte>();
        for(int i=0;i<l.size();i++){
            if(l.get(i).getClient()==c){
                cc.add(l.get(i));
            }
        }
        return cc;
    }
}
