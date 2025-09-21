package pobj.pkgman;

import java.util.List;

public class LimitPkg extends AbstractPkg implements IPkg{
	private static int cpt = 0;
	
	public LimitPkg(String nom, IVersion version, List<IPkg> dependencies) {
		super(nom, version, dependencies);
	}
	
	public static int getNbInstalled() {
		return cpt;
	}

	@Override
	public String getName() {
		return this.getNom();
	}

	@Override
	public IVersion getVersion() {
		return this.getVers();
	}

	@Override
	public List<IPkg> getDependencies() {
		return this.getDep();
	}

	@Override
	public boolean install() {
		if(cpt>=10) {
			return false;
		}
		cpt++;
		return true;
	}

	@Override
	public void uninstall() {
		cpt--;
	}

}
