package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import pobj.pkgman.IPkg;
import pobj.pkgman.ISimplePkg;
import pobj.pkgman.SimplePkgAdapter;

public class SimplePkgAdapterTest {
	
	class SimplePkg implements ISimplePkg {

		@Override
		public String name() {
			return "name";
		}

		@Override
		public void install() {
		}
		
	}
	
	@Test public void test() {
		ISimplePkg spkg = new SimplePkg();
		IPkg pkg = new SimplePkgAdapter(spkg);
		assertEquals("name", pkg.getName());
		assertEquals(1, pkg.getVersion().getMajor());
		assertTrue(pkg.getDependencies().isEmpty());
		assertTrue(pkg.install());
	}
	
}
