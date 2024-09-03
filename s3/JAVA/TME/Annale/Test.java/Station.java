import java.util.ArrayList;

public class Station{
    private String nom;
    public int energie;
    public int materiaux;
    private ArrayList<Module> structure;
    private ArrayList<Alimentable> aAlimenter;

    public Station(String name){
        nom=name;
        energie=0;
        materiaux=100;
        structure= new ArrayList<Module>();
        aAlimenter= new ArrayList<Alimentable>();
    }

    public void Construire(Construction c ) {
        if (materiaux< c.getCout()){
            System.out.println("Ressources insuffisantes");
        }else{
            materiaux-= c.getCout();
            if((Module)c instanceof Module){
                structure.add((Module) c);
                if( c instanceof Alimentable){
                    aAlimenter.add((Alimentable) c);
                }
            }
            System.out.println("Construction de "+c.toString());
        }
    }

    public void phaseProduction(){
        energie=0;
        for(Module m: structure){
            m.produire(this);
        }
    }

    public void phaseAlimentation(){
        for(Alimentable a: aAlimenter){
            while(energie>0){
                System.out.println("Coupure de courant");
                a.alimenter(this);
            }
        }
    }

    public void brancher(Alimentable a){
        aAlimenter.add(a);
    }

    public void debrancher(Alimentable a){
        aAlimenter.remove(a);
    }

    public int getMateriaux(){
        return materiaux;
    }
    public int getEnergie(){
        return energie;
    }
    public void addEnergie(int a){
        energie-=-a;
    }
    public String toString(){
        return nom+" ("+energie+" kW, "+materiaux+" materiaux)";
    }
}