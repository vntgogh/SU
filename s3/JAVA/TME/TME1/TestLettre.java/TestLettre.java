public class TestLettre {
    public static void main(String[] args){
        for (char i='a'; i<='z';i++){
            Lettre i1= new Lettre(i); //on crée des objets de type Lettre car la méthode getCodeAscii n'est accessible que pour les types Lettre
            System.out.println("Le code ASCII de "+i+" est "+i1.getCodeAscii());
        }
        for (char i='a'; i<='z';i++){
            Lettre i1= new Lettre(i); 
            System.out.println(i1.getCarac()+" ");
            if((i-'a')%5 == 4){
                System.out.println();
            }
        }
    }
}
