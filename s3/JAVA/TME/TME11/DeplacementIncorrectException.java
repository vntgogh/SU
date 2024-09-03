public class DeplacementIncorrectException extends Exception{
    public DeplacementIncorrectException(int x,int y){
        super("Erreur : Deplacement impossible en ("+x+","+y+")");
    }
}
