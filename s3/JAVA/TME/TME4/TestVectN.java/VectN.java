import java.util.Random; 

public class VectN{
    private int[] tab;

    private VectN(int n){
        this.tab= new int[n];
    }

    public VectN(int n, int ValMax){
        this(n); // création d'un vecteur de taille n
        Random random = new Random();
        for (int i=0; i<n; i++){ // assignation des valeurs du tableau
            tab[i] = random.nextInt(ValMax+1); //(int)Math.random()*(ValMax+1) est mal interprétée à cause des opérations et du cast
        }
    }

    public VectN(){
        this(5,9);
    }

    public VectN(int a, int b, int c){
        this(3);
        tab[0]=a;
        tab[1]=b;
        tab[2]=c;
    }

    public void affiche(){
        System.out.print("[");
        int i=0;
        for (int val : tab){
            System.out.print(val);
            if (i < tab.length -1) {
                System.out.print(", ");
            }
            i++;
        }
        System.out.print("]\n");
    }

    public int somme(){
        int s=0;
        for(int val : this.tab){
            s+= val;
        }
        return s;
    }

    public String toString(){
        StringBuilder strBuild = new StringBuilder("[");
        for(int i=0; i<tab.length; i++){
            strBuild.append(tab[i]);
            if (i < tab.length - 1) {
                strBuild.append(", ");
            }
        }
        strBuild.append("]");
        return strBuild.toString();
    }

    public int[] getTab(){
        return this.tab;
    }
    
    public int[] getTabCopie(){
        int[] newtab = new int[this.tab.length];
        int i=0;
        for(int val : this.tab){
            newtab[i]= val;
            i++;
        };
        return newtab;
    }
}