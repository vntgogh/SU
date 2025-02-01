package pobj.pkgman.log;

import java.util.List;

import pobj.pkgman.IPkg;
import pobj.pkgman.IVersion;

public class PkgLogger implements IPkg{
	private IPkg pk;
	private ILogger lo;
	
	public PkgLogger(IPkg pkg, ILogger log) {
		this.pk =pkg;
		this.lo =log;
	}
	
	@Override
	public String getName() {
		return pk.getName();
	}

	@Override
	public IVersion getVersion() {
		return pk.getVersion();
	}

	@Override
	public List<IPkg> getDependencies() {
		return pk.getDependencies();
	}

	@Override
	public boolean install() {
		lo.log("Installing paquet-"+pk.getVersion().getMajor()+"."+pk.getVersion().getMinor());
		boolean b = pk.install();
		if(b) {
			lo.log("Success");
			return true;			
		}
		lo.log("Failure");
		return false;
	}

	@Override
	public void uninstall() {
		pk.uninstall();
		lo.log("Uninstalling paquet-"+pk.getVersion().getMajor()+"."+pk.getVersion().getMinor());
	}

}
