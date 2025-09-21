import java.util.ArrayList;

public class Panier extends ArrayList<Ramass>{
    public double max;

    public Panier(double maxPoids){
        max=maxPoids;
    }

    public double getPoids(){
        double sum= 0;
        for (Ramass val : this){
            sum += val.getPoids();
        }
        return sum;
    }
    
    @Override public boolean add(Ramass o){
        if(this.getPoids()+o.getPoids()<= this.max){
            super.add(o);
            System.out.println(o.toString()+" est ajouté au panier");
            return true;
        }else{
            System.out.println(o.toString()+" n'est pas ajouté au panier");
            return false;
        }
    }

    public int compterToxic(){
        int cpt=0;
        for (Ramass val: this){
            if(val instanceof Toxic){
            //&& ((Toxic)val).estToxic()){
                cpt++;
            }
        }
        return cpt;
    }
    
    public String toString(){
        String res="Panier contenant "+this.size()+" objets, dont "+this.compterToxic()+" ("+this.getPoids()+" sur "+max+")";
        return res;
    }

}