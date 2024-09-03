
    public class Client { 
    private static int compteur = 0; 
    private int id; 
    private final String nom; 
    private final String prenom; 
    private int nbOperations; 

    public Client(String nom, String prenom) { 
        id = compteur++; 
        this.nom = nom; 
        this.prenom = prenom; 
        nbOperations = 0; 
    }
    public String getNom() { return nom; } 

    public String getPrenom() { return prenom; } 

    public void enregistreOperation() { nbOperations++; } 

    @Override public String toString() { 
        return "Client(nom=" + nom + ", prénom=" + prenom + ", nbOps=" + nbOperations + ")"; 
    } 
    @Override public boolean equals(Object o) { 
        if (o == this) 
        return true; 
        if (!(o instanceof Client)) 
        return false; 
        Client c = (Client)o; 
        return (c.nom.equals(nom) && c.prenom.equals(prenom)); 
    } 
} 