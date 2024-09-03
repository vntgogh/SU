public class Villageois{
    private String nom;
    private double poids;
    private boolean malade;
    public Villageois(String nomVillageois){
        nom = nomVillageois;
        poids = Math.random()*(100)+50;
        malade = Math.random()<0.2;
    }
    public String toString(){
        String OuiNon = "";
        if (malade){
            OuiNon= "oui";
        }else{
            OuiNon= "non";
        }
        String poidsString = String.format("%.2f", poids);
    
        String s = "villageois : " + nom + ", poids : " + poidsString + " kg, malade : " + OuiNon+ ", peut soulever "+PoidsSouleve()+ " kg.";
        return s;
    }
    public String getNom(){
        return nom;
    }
    public double getPoids(){
        return poids;
    }
    public boolean getMalade(){
        return malade;
    }
    public double PoidsSouleve(){
        if (malade){
            return poids/4;
        }else{
            return poids/3;
        }
    }
}