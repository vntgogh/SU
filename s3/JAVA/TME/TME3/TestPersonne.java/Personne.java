
import java.util.Random;

public class Personne{
    private String nom;
    private Personne conjoint;
    public Personne(String name){
        this.conjoint=null;
        this.nom=name;
    }

    public Personne(){  
        Random random = new Random();
        char randomLetter = (char) (random.nextInt(26) + 'A');
        this.nom="Pers"+randomLetter;
        this.conjoint=null;
    }
    
    public String toString(){
        if (this.conjoint == null){
            return this.nom+", célibataire";
        }else{
            return this.nom+", marié";
        }
    }

    public void setConjoint(Personne conjoint){
        this.conjoint = conjoint;
    }

    public void epouser(Personne pe){
        if((this.conjoint !=null) || (pe.conjoint !=null) || (this == pe) || (pe==null)){
            System.out.println( "Le mariage de "+ this.toString()+" avec "+pe.toString()+", est impossible");
        }else{
            
            System.out.println(this.toString()+" se marie avec "+pe.toString());
            this.setConjoint(pe);
            pe.setConjoint(this);
        }
    }

    public void divorcer(){
        if (this.conjoint == null){
            System.out.println("Ce divorce est impossible");
        }else{
            System.out.println(this.toString()+" divorce de "+this.conjoint.toString());
        }
        this.conjoint=null;
    }
}