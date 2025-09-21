
import java.util.ArrayList;

public class Foret {
    private Object[][] terrain;
    
    public Foret(int taille){
        terrain= new Object[taille][taille];
    }

    public boolean placer(Object o){
        if (o instanceof Arbre || o instanceof Champignon){
            int x=(int)(Math.random()*(terrain.length));
            int y=(int)(Math.random()*(terrain.length));
            terrain[x][y]=o;

            if (terrain[x][y]==o) return true;
        }
        return false;
    }
    
    public String toString(){
        String res = "";

        for(int i=0; i<terrain.length; i++){
            res+="|";
            for (int j=0; j<terrain[i].length; j++){
                if (terrain[i][j]==null){
                    res+=" ";
                }else{
                    res+= terrain[i][j].toString().charAt(0);
                }
            }
            res+="|\n";
        }
        return res;
    }
     public ArrayList<Champignon> ramasserChampignons(){

        ArrayList<Champignon> lchamp= new ArrayList<Champignon>();

        for(int i=0; i<terrain.length; i++){
            for (int j=0; j<terrain[i].length; j++){
                if(terrain[i][j] instanceof Champignon){
                    lchamp.add((Champignon)terrain[i][j]);
                    terrain[i][j]=null; //enleve l'objet du terrain
                }
            }
        }
        return lchamp;
     }

     public ArrayList<Ramass> ramasserTout(){

        ArrayList<Ramass> l= new ArrayList<Ramass>();

        for(int i=0; i<terrain.length; i++){
            for (int j=0; j<terrain[i].length; j++){
                if(terrain[i][j] instanceof Ramass){
                    l.add((Ramass)terrain[i][j]);
                    terrain[i][j]=null;
                }
            }
        }
        return l;
     }

     public void ramasser(Panier p){

        for(int i=0; i<terrain.length; i++){
            for (int j=0; j<terrain[i].length; j++){
                if(terrain[i][j] instanceof Ramass){
                    p.add((Ramass)terrain[i][j]);
                    terrain[i][j]=null;
                }
            }
        }
     }
}
