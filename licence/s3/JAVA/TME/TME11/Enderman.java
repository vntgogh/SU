public class Enderman extends Gardien implements Teleportation{

    public Enderman(int quant){
        super("Enderman",quant);
    }

    public void EnderTeleportation(Grille g) throws DeplacementIncorrectException{
    
            
        int x=(int)(Math.random()*g.nbLignes);
        int y=(int)(Math.random()*g.nbColonnes);

        try {
                while((g.sontValides(x,y)==false) || (x==this.getX() && y==this.getY())){
                    x=(int)(Math.random()*(g.nbLignes));
                    y=(int)(Math.random()*g.nbColonnes);
                }
                System.out.println(this.toString()+" s'est téléporté en ("+x+","+y+")");
                g.videCase(this.getX(),this.getY()); //vide l'ancien emplacement de l'Enderman
                
                g.setCase(x,y,this); //place l'Enderman sur la grille

                this.setPosition(x,y); //met à jour les coordonénes de l'Enderman

                // cas où un agent se toruve sur le nouvel emplacement de l'Enderman

        } catch (CoordonneesIncorrectesException e) {
            System.out.println(e.getMessage());
            throw new DeplacementIncorrectException(x,y);
        } catch(CaseNonPleineException e ){
            System.out.println(e.getMessage());
            throw new DeplacementIncorrectException(x,y);
        }
    }
}