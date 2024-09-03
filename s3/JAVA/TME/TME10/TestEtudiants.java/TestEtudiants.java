import java.util.ArrayList;

public class TestEtudiants{
    public static void main (String[] args){

        ArrayList<Etudiant> le = new ArrayList<Etudiant>();

        Etudiant e1= null;
        for (int i=0; i< args.length; i++){
            try{
                int n = Integer.parseInt(args[i]);
                //System.out.println(n+" est une note");
                e1.entrerNote(n);

            }catch(NumberFormatException e){
                //System.out.println(args[i]+" est un nom");
                e1= new Etudiant(args[i]);            
                le.add(e1);
            }catch( TabNotesPleinException e){
                System.out.println("le tableau de l'étudiant "+e1+" "+e.getMessage());
            }
        }
        System.out.print("les "+le.size()+" étudiants : ");
        System.out.print("[");
        for (int k=0; k<le.size(); k++){
            System.out.print(le.get(k));
            if(k<le.size()-1){
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }
}