import java.util.ArrayList;

public class Agent6{
    private int x;
    private int y;
    private ArrayList <Joyau> sac;
    private Grille g;
    private static Agent6 instance;


    private  Agent6(int x,int y,Grille g) throws CoordonneesIncorrectesException{
        if(g.sontValides(x,y)){
            this.x=x;
            this.y=y;
            this.sac=new ArrayList<Joyau>();
            this.g=g;
        }else{
            throw new CoordonneesIncorrectesException(x,y);
        }  
    }

    public static Agent6 getInstance(int x,int y,Grille g){
        if(instance==null){
            try {
                instance=new Agent6(x, y, g);
                System.out.println("Une instance a été crée");
                return instance;
            } catch (CoordonneesIncorrectesException e) {
                System.out.println(e.getMessage());
                return null;
            }
        }
        System.out.println("On a déjà une instance");
        return instance;
}
    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }

    

    public void seDeplacer(int xnew,int ynew) throws DeplacementIncorrectException {
        /*Si il y a un gardien a la case je perd mes joyaux */
        if(this.g.sontValides(xnew,ynew)){
            this.x=xnew;
            this.y=ynew;
            try {
                if(g.caseEstVide(xnew,ynew)==false){
                    Contenu in =g.getCase(xnew,ynew);
                    if(in instanceof Joyau){
                        System.out.println(in.toString()+" a été récupéré.");
                        this.remplirSac((Joyau)g.videCase(xnew,ynew));
                        
                    }else{
                        Gardien ga=(Gardien)g.getCase(xnew,ynew);
                        System.out.println("L'agent Steve croise "+ga.toString()+" et perd tout ses joyaux ! ");
                        this.videSac();
                    }
            }
            } catch (CoordonneesIncorrectesException e) {
                System.out.println(e.getMessage());
                throw new DeplacementIncorrectException(xnew,ynew);
            } catch(CaseNonPleineException e ){
                System.out.println(e.getMessage());
            
            }

        }else{
            throw new DeplacementIncorrectException(xnew,ynew);
        }
    }


    public void seDeplacer(int xnew,int ynew,int f) throws DeplacementIncorrectException{
        if(g.sontValides(xnew,ynew)){
            this.x=xnew;
            this.y=ynew;
            try {
                if(g.caseEstVide(xnew,ynew)==false){
                    Contenu in =g.getCase(xnew,ynew);
                    if(in instanceof Joyau){
                        this.remplirSac((Joyau)g.videCase(xnew,ynew));
                        
                    }else{
                        Gardien ga=(Gardien)g.getCase(xnew,ynew);
                        System.out.println("L'agent Steve croise "+ga.toString());
                        if(ga.getPdv()<=f){
                            System.out.println("Le gardien "+ga.toString()+" a été vaincu ");
                            g.videCase(xnew,ynew);
                        }else{
                            System.out.println("Le gardien "+ga.toString()+" a vaincu l'agent et il a perdu "+f+" PV!");
                            ga.pertePV(f);
                            this.videSac();
                        }
                        
                    }
            }
            } catch (CoordonneesIncorrectesException e) {
                System.out.println(e.getMessage());
                throw new DeplacementIncorrectException(xnew,ynew);
            } catch(CaseNonPleineException e ){
                System.out.println(e.getMessage());
                throw new DeplacementIncorrectException(xnew,ynew);
            }
    }else{
        throw new DeplacementIncorrectException(xnew,ynew);
    }

}
    public int fortune(){
        int out=0;
        for(int i=0;i<sac.size();i++){
            out+=sac.get(i).getnbpieces();
        }
        return out;
    }
    public void contenuSac(){
        for(int i=0;i<sac.size();i++){
            System.out.println(sac.get(i).toString());
        }
    }
    public void remplirSac(Joyau j){
        this.sac.add(j);
    }
    public void videSac(){
        int i=0;
        while(i<sac.size()){
            sac.remove(0);
            i++;
        }

    }

    public String toString(){
        return ("L'agent Steve en ("+this.x+","+this.y+") avec un sac contenant "+this.sac.size()+" joyaux");
    }
    
}
