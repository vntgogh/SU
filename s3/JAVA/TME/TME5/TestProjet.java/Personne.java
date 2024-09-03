public class Personne {
    private static int nbPers;
    private String nom;
    private static char lettre='A';

    public Personne(){
        this.nom="Individu"+((char)(lettre+nbPers));
        nbPers++;
    }

    public static int getNbPers(){
        return nbPers;
    }

    public String toString(){
        return this.nom;
    }
}