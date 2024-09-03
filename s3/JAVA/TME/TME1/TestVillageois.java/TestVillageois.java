public class TestVillageois{
    public static void main(String[] args){
        Villageois v1 = new Villageois("Yuji");
        Villageois v2 = new Villageois("Gojo");
        Villageois v3 = new Villageois("Geto");
        Villageois v4 = new Villageois("Toji");
        System.out.println(v1.toString()+"\n"+v2.toString()+"\n"+v3.toString()+"\n"+v4.toString());
        System.out.println(v1.getNom()+", "+v1.getPoids()+", "+v1.getMalade()+"\n"+
                            v2.getNom()+", "+v2.getPoids()+", "+v2.getMalade()+"\n"+
                            v3.getNom()+", "+v3.getPoids()+", "+v3.getMalade()+"\n"+
                            v4.getNom()+", "+v4.getPoids()+", "+v4.getMalade()+"\n");
        double PoidsTotal =v1.PoidsSouleve()+v2.PoidsSouleve()+v3.PoidsSouleve()+v4.PoidsSouleve();
        if ((PoidsTotal)>=100){
            System.out.println("Poids Total : "+PoidsTotal+".\n Le rocher est soulevé !");
        }else{
            System.out.println("Poids Total : "+PoidsTotal+".\n Le rocher ne peut être soulevé :(");
        }
    }
}