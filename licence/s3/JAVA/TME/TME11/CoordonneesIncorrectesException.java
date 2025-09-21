public class CoordonneesIncorrectesException extends Exception {
    public CoordonneesIncorrectesException(int x,int y){
        super("Erreur: coordonnees ("+x+", "+y+") incorrectes !");
    }
}

