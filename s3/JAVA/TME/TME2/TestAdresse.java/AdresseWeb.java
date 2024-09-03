
public class AdresseWeb{
    private String protocole, domaine, chemin;

    public AdresseWeb(String prot, String dom, String chem){
        this.protocole=prot;
        this.domaine=dom;
        this.chemin=chem;
    }
    public AdresseWeb(String dom, String chem){
        this("http",dom,chem);
    }
    public AdresseWeb(String chem){
        this("http", "", chem);
    }
    public String toString(){
        return this.protocole+"://www."+this.domaine+this.chemin;
    }
}