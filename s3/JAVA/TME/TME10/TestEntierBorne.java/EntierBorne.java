public class EntierBorne{
    private int valeur;
    private static final int MIN=-100, MAX=100;

    public EntierBorne(int x) throws HorsBorneException{
        if(x<MIN){
            throw new HorsBorneException("Entier trop petit : "+x);
        }
        if(x>MAX){
            throw new HorsBorneException("Entier trop grand : "+x);
        }
        valeur=x;
    }

    public String toString(){
        return "valeur:"+valeur;
    }

    public EntierBorne somme(EntierBorne eb) throws HorsBorneException{
        int sum=valeur+eb.valeur;
        return new EntierBorne(sum);
    }

    public EntierBorne divPar(EntierBorne eb) throws DivParZero, HorsBorneException{
        if(eb.valeur == 0){
            throw new DivParZero();
        }
        int div=(int)(valeur/eb.valeur);
        return new EntierBorne(div);
    }
}