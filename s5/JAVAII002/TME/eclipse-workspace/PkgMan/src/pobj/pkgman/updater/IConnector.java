package pobj.pkgman.updater;

public interface IConnector {
	
	/** 
	 * Retourne une nouvelle base de paquets.
	 * Retourne null en cas d'échec de création.
	 */
	public IDatabase getDatabase();
}
