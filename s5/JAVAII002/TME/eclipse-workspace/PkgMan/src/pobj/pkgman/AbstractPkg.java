package pobj.pkgman;

import java.util.List;

public abstract class AbstractPkg implements IPkg{
	private String nom;
	protected IVersion v;
	private List<IPkg> l;
	
	public AbstractPkg(String nom, IVersion version, List<IPkg> dependencies) {
		this.nom=nom;
		this.v=version;
		this.l=dependencies;
	}
	
	public IVersion getVers() {
		return this.v;
	}
	
	public String getNom() {
		return this.nom;
	}
	
	public List<IPkg> getDep(){
		return this.l;
	}
	
	public String toString() { 
		return this.nom+"-"+this.getVersion().toString();
	}
	
	public abstract boolean install();
	public abstract void uninstall();

}
