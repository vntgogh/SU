public class TestEntierBorne{
    public static void main(String[] args){
        

        /*EntierBorne ebX=new EntierBorne(x);
        EntierBorne ebY=new EntierBorne(y);
        EntierBorne s=ebX.somme(ebY);
        System.out.println("somme de ebX et ebY, "+s.toString());
        System.out.println(x);
        System.out.println(y);

        throw new HorsBorneException("Hors borne!");*/

        try{        
            int x=(int)(Math.random()*3);
            int y=(int)(Math.random()*(301)-150);
            EntierBorne ebX=new EntierBorne(x);
            EntierBorne ebY=new EntierBorne(y);
            EntierBorne s=ebX.somme(ebY);
            EntierBorne d=ebX.divPar(ebY);

            System.out.println("ebX : " +ebX.toString());
            System.out.println("ebY : " +ebY.toString());
            System.out.println("ebX+ebY, "+s.toString());
            System.out.println("ebX/ebY, "+d.toString());

        }catch(DivParZero e){
            System.out.println(e.getMessage());
        }catch(HorsBorneException e){
            System.out.println(e.getMessage());
        }
    }
}


//65.7 
// a) remplacer HorsBorneException e par Exception e rend le catch(DivParZero inutile car 
// il est déja traité dans Exception e)le main ne compile donc pas mais s'exécute
// b) il est possible de rassembler toutes les exceptions dans un catch(Exception e)
// il est cependant moins intéressant car il ne permet pas de distinguer chaque exception et d'afficher 
// le message spécifique de chacune d'elle
// c) il est possible de rajouter un simple throws Exception à la suite de la signature du main
// il est néanmoins pas recommandé de le faire car cela renvoie toutes les exceptions dont celles non-sollicitées