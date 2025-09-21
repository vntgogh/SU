package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Collections;

import org.junit.Test;

import pobj.pkgman.IPkg;
import pobj.pkgman.LimitPkg;
import pobj.pkgman.Version;

public class LimitPkgTest {

	@Test public void test() {
		IPkg pkg = new LimitPkg("paquet", new Version(2,0), Collections.emptyList());
		assertEquals("paquet", pkg.getName());
		assertEquals(2, pkg.getVersion().getMajor());
		assertTrue(pkg.install());
		assertEquals(1, LimitPkg.getNbInstalled());
	}
	
}
