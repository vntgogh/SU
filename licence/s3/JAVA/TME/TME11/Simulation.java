import java.util.ArrayList;

public class Simulation {
    private Agent6 a;
    private Grille g;
    private ArrayList<Contenu> list=new ArrayList<Contenu>();
    private ArrayList<Enderman> listEnder=new ArrayList<Enderman>();

    public Simulation(Agent6 a,Grille g,int m)throws CoordonneesIncorrectesException{
        this.g=g;
        this.a=a;
        int clone=0;
        while(m>0){
            m-=1;
            double alea=Math.random();
            if(alea>0.5){
                double aleaJ=Math.random();
                if(aleaJ<0.25){
                    list.add(new Joyau("Fer", (int)(aleaJ*10)));
                }else if(aleaJ>=0.25 && aleaJ<0.5){
                    list.add(new Joyau("Or", (int)(aleaJ*5)));
                }else if(aleaJ>=0.5 && aleaJ<0.75){
                    list.add(new Joyau("Emeraude", (int)(aleaJ*5)));
                }else{
                    list.add(new Joyau("Diamant", 1));
                }

            }else{
                double aleaJ=Math.random();
            
                if(aleaJ>0.90){
                    Enderman e=new Enderman(1);
                     list.add(e);
                     listEnder.add(e);
                     
                }else{
                    list.add(new Gardien(1));
                    if (clone==0 && m!=0){
                        System.out.println("Le Gardien "+((Gardien)list.get(list.size()-1)).toString()+"a ete cloné");
                        list.add(new Gardien((Gardien)list.get(list.size()-1))); 
                        System.out.println("Le Gardien "+((Gardien)list.get(list.size()-1)).toString()+"est un clone");
                        clone=1;
                    }
                }
            }
        }


            try{
                for(int i=0;i<list.size();i++){
                int x=(int)(Math.random()*(this.g.nbLignes));
                int y=(int)(Math.random()*(this.g.nbColonnes));
                while(g.caseEstVide(x,y)==false){
                    x=(int)(Math.random()*(this.g.nbLignes));
                    y=(int)(Math.random()*(this.g.nbColonnes));
                }
                list.get(i).setPosition(x,y);
                this.g.setCase(list.get(i).getX(),list.get(i).getY(),list.get(i));
            }
        
            }catch(CoordonneesIncorrectesException e){
                System.out.println(e.getMessage());
            }
        }

    

    public String toString(){
        String out="";
        for(int i=0;i<list.size();i++){
            out+=list.get(i).toString()+"\n";
        }
        return out;
    }

    public void lance(int nbEtapes)throws DeplacementIncorrectException{
        System.out.println("\nQue la simulation du minage Minecraft commence !!!!");
        while(nbEtapes>0){
            nbEtapes--;
            double alea=Math.random();
            int xdir=(int)(Math.random()*(3))-1;
            int ydir=(int)(Math.random()*(3))-1;
            int xnew=a.getX()+xdir;
            int ynew=a.getY()+ydir;
            while(g.sontValides(xnew,ynew)==false || (xdir==0 && ydir==0)){
                 xdir=(int)(Math.random()*(3))-1;
                 ydir=(int)(Math.random()*(3))-1;
                 xnew=a.getX()+xdir;
                ynew=a.getY()+ydir;    
            }

            if(alea<=0.3){
                int f=(int)(Math.random()*(100-10+1))+10;
                try {
                    System.out.println(a.toString()+" s'est déplacé en ("+xnew+","+ynew+")");
                    for(int i=0;i<listEnder.size();i++){
                        listEnder.get(i).EnderTeleportation(this.g);
                        
                    }
                    a.seDeplacer(xnew,ynew, f);
                } catch (DeplacementIncorrectException e) {
                    System.out.println(e.getMessage());
                    break;
                }
            }else{
                try {
                    System.out.println(a.toString()+" s'est deplacé en ("+xnew+","+ynew+")");
                    a.seDeplacer(xnew,ynew);
                } catch (DeplacementIncorrectException e) {
                    System.out.println(e.getMessage());
                    break;
               }
            }
          g.affiche(10);
        }
    System.out.println(a.toString()+" a fini son expédition, il est ressorti avec une fortune de "+a.fortune()+" pièces d'or !");

    }


}
