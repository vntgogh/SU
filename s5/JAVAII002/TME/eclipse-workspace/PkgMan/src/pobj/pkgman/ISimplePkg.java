package pobj.pkgman;

public interface ISimplePkg {
	
	/** Retourne le nom du paquet. */
	public String name();
	
	/** Installe le paquet. N'échoue jamais. */
	public void install();
}
