public class Etudiant{
    private String nom;
    private int[] tabnotes;
    public static final int MAX = 5;
    private int cpt;

    public Etudiant(String n){
        nom=n;
        tabnotes=new int[MAX];
        cpt=0;
    }

    public void entrerNote(int note) throws TabNotesPleinException{
        if(cpt< MAX){
            tabnotes[cpt]= note;
            cpt++;
        }else{
            throw new TabNotesPleinException();
        }
    }

    public String toString(){
        String notes="";
        for(int i=0; i<cpt;i++){
            notes+=tabnotes[i];
            if ( i<cpt-1){
                notes+=" ";
            }
        }
        return nom+" "+notes;
    }
}