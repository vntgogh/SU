public class TestSegment {
    public static void main(String[] args){
        Segment s1= new Segment(6,8);
        Segment s2= new Segment(12,5);
        int ls1= s1.longueur();
        int ls2= s2.longueur();
        if (ls1<ls2){
            System.out.println("Le segment s2 est plus long. "+s2.toString());
        }else{
            System.out.println("Le segment s1 est plus long. "+s1.toString());
        }
    }
}
