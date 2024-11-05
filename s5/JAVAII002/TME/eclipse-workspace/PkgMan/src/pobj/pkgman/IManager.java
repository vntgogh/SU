package pobj.pkgman;

import java.util.List;

public interface IManager {
	
	/** 
	 * Installe le paquet 'pkg' et toutes ses dépendances.
	 * Retourne 'true' si toutes les installations ont réussi, 'false' sinon.
	 */
	public boolean installPkg(IPkg pkg);
	
	/** Déinstalle le paquet 'pkg'. Les dépendances ne sont pas touchées. */
	public void uninstallPkg(IPkg pkg);
	
	/** Retourne la liste des paquets installés. */
	public List<IPkg> getInstalled();
}
