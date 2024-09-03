public class CaseNonPleineException extends Exception {
    public CaseNonPleineException(int x,int y){
        super("Dans la case ("+x+","+y+"): null");
    }
}
