public class SystemeSolaire{
    public static void main(String[] args){
        Planete m = new Planete("Mercure", 2439.7);
        Planete t = new Planete("Terre", 6378.137);
        System.out.println(m.toString());
        System.out.println("Le rayon de la Terre est "+t.getRayon());
    }
}