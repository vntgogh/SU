

public class Pile{
    private Assiette[] tabass;
    private int nbA;

    public Pile(int tailleMax){
        this.tabass= new Assiette[tailleMax]; //tab.length = tailleMax
        nbA=0;
    }

    public  boolean estVide(){
        return nbA == 0;
    }

    public boolean estPleine(){
        return nbA == this.tabass.length; 
    }

    public void empiler(Assiette a){
        if(this.estPleine()==false){
            this.nbA++;
            this.tabass[nbA-1] = a;
        }else{
            System.out.println("pile pleine, impossible d'ajouter une assiette");
        }
    }

    public Assiette depiler(){
        Assiette ad;
        if(this.estVide()==true){
            System.out.println("Tableau vide");
            return null;
        }else{
            this.nbA--;
            ad = tabass[nbA];
        }return ad;
    }

    public String toString(){
        if(this.nbA==0){
            return "()";
        }
        StringBuilder strBuild = new StringBuilder("Pile : ");
        /*for (int i=this.tabass.length -1; i>=0; i--){
            strBuild.append("<"+tabass[i].toString()+">");
            if (i>0){
                strBuild.append(", ");
            }
        }*/
        for (int i=0; i<this.nbA; i++){
            if (this.tabass[i]!=null){
                strBuild.append("<"+this.tabass[i]+">");
                if (i<this.nbA-1){
                    strBuild.append(", ");
                }
            }
        }
        return strBuild.toString();
    }
}