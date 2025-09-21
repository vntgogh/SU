import javax.swing.text.Style;

public class Menagerie{
    private static int cpt=0;
    private Animal[] tab;

    public Menagerie(int tmax){
        tab=new Animal[tmax];
    }

    public void ajouter(Animal a){
        if(cpt<tab.length){
            this.tab[cpt]=a;
            cpt++;
        }else{
            System.out.println("Plus de place dans cette ménagerie :( \n");
        }
    }

    public String toString(){
        StringBuilder sb=new StringBuilder("Ménagerie : \n");
        for(int i=0; i<cpt;i++){
            sb.append("tab["+i+"] = "+tab[i]+"\n");
        }
        return sb.toString();
    }

    public void midi(){
            for (int i =0; i<cpt; i++){
                System.out.println(tab[i].toString()+tab[i].crier());
            }
    }

    public void vieillirTous(){
        for(int j=0; j<cpt;j++){
            tab[j].vieillir();
        }
    }
}