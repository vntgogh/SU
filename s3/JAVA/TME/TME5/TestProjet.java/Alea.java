public class Alea {
    private Alea(){}

    public static char lettre(){
        return (char)('a'+Math.random()*26);
    }

    public static String chaine(){
        StringBuilder ch=new StringBuilder("");
        for (int i=0;i<10;i++){
            ch.append(Alea.lettre());
        }
        return ch.toString();
    }
}

// question 2 : lettre() et chaine() sont des variables de classe car elles ne dépendent pas des instances et leurs attributs mais de la classe 
// de plus, elles pourront etre accessibles dans toute la classe, lettre() est utile paar exemple pour générer une chaine chaine()

// question 3 : pour empêcher la création d'instances, on peut créer un constructeur private sans paramètre