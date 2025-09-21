package pobj.pkgman;

import java.util.ArrayList;
import java.util.List;

public class Manager {
	private List<IPkg> paq;

	public Manager() {
		paq = new ArrayList<IPkg>();
		
	}
	
	public List<IPkg> getInstalled() {
		return this.paq;
	}
	
	public boolean installPkg(IPkg pkg) {
		if(paq.contains(pkg)) return true;
		this.paq.add(pkg);
		for(IPkg d : pkg.getDependencies()) {
			if(!paq.contains(d)) {
				boolean b = this.installPkg(d);
				if(!b) return false;
			}
		}
		return true;		
	}
	
	public void uninstallPkg(IPkg pkg) {
		if(!paq.contains(pkg)) return;
		for(int i=0;i<this.paq.size();i++) {
			if(this.paq.get(i)==pkg) {
				this.paq.remove(i);
			}
		}
	}
}
