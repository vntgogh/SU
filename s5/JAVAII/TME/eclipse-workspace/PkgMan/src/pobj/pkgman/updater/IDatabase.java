package pobj.pkgman.updater;

import pobj.pkgman.IPkg;

public interface IDatabase {
	
	/**
	 * Retourne la dernière version disponible du paquet de nom 'name' dans la base.
	 * Retourne null si aucun paquet de ce nom n'existe dans la base.
	 */
	public IPkg getPackage(String name);
	
	/** 
	 * Ferme la base.
	 * getPackage ne peut plus être appelé après la fermeture.
	 */
	public void close();
}
