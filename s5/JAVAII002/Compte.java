public class Compte{
	private static int compteur = 0; 
	private int id; 
	private double solde;
	private Client client;

	public Compte(Client c, double s){
		id = compteur++;
		this.solde = s;
		this.client = c;
	}
	
	public Client getClient(){ return this.client;}
	public double getSolde(){ return this.solde;}
	public void crediter(double somme){ this.solde += somme; }
	public void debiter(double somme){ this.solde -= somme; }
	public boolean equals(Compte com){
        if (this.id==com.id){return true;}
		return false;
    }
    public String toString(){return "id="+id+", client="+client+", solde="+solde;}
}