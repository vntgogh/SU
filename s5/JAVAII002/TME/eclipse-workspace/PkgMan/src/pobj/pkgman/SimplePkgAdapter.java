package pobj.pkgman;

import java.util.ArrayList;
import java.util.List;

public class SimplePkgAdapter implements IPkg{
	private ISimplePkg sp;
	
	public SimplePkgAdapter(ISimplePkg sp) {
		this.sp=sp;
	}
	
	@Override
	public String getName() {
		return this.sp.name();
	}

	@Override
	public IVersion getVersion() {
		return Version.getDefaultVersion();
	}

	@Override
	public List<IPkg> getDependencies() {
		return new ArrayList<IPkg>();
	}

	@Override
	public boolean install() {
		this.sp.install();
		return true;
	}

	@Override
	public void uninstall() {
		return;
	}
}
