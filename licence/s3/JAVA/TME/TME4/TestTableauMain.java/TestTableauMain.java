// Exercice 26

public class TestTableauMain{
    public static void main(String[] args){
        int nb_args=0;
        for (String arg : args){
            nb_args++; 
        }
        System.out.println("Il y a "+nb_args+" arguments.");
        int cpt=0;
        for (String arg : args){
            cpt++;
            System.out.println("arg["+(cpt-1)+"] = "+args[cpt-1]); 
        }
    }
}

