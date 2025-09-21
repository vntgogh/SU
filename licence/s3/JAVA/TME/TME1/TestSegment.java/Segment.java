public class Segment {
    private int x;
    private int y;
    public Segment(int extX, int extY){
        x= extX;
        y= extY;
    }
    public int longueur(){
        if ((x-y)<0){
            return y-x;
        }else{
            return x-y;
        }
    }    
    public String toString(){
        return "Segment ["+x+","+y+"]";
    }
}
