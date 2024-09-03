public class Projet {
    private String np;
    private Trio t=new Trio();
    private static int nbPr=0;

    public Projet(String nomp){
        this.np=nomp;
        nbPr++;
    }

    public Projet(){
        this(Alea.chaine());
    }

    public String toString(){
        return "Projet "+this.np+" "+t.toString();
    }

    public static int getNbProjet(){
        return nbPr;
    }
}
