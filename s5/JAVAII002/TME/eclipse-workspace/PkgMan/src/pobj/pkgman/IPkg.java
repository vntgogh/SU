package pobj.pkgman;

import java.util.List;

public interface IPkg {
	
	/** Retourne le nom du paquet. */
	public String getName();
	
	/** Retourne la version du paquet. */
	public IVersion getVersion();
	
	/** Retourne la liste de dépendances du paquet. */
	public List<IPkg> getDependencies();

	/** 
	 * Installe un paquet.
	 * Retourne true en cas de succès, false en cas d'échec.
	 */
	public boolean install();
	
	/**
	 * Désinstalle un paquet
	 * N'échoue jamais.
	 */
	public void uninstall();
	
	/** 
	 * Comparaison d'égalité.
	 * Le nom et le numéro de version de this et de o doivent correspondre.
	 */
	public boolean equals(Object o);
	
	/** Conversion en chaîne de la forme nom-version. */
	public String toString();
}
