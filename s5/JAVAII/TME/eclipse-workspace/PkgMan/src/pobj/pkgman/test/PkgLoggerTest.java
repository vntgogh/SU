package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;

import java.util.Collections;

import org.junit.Test;

import pobj.pkgman.IPkg;
import pobj.pkgman.LimitPkg;
import pobj.pkgman.Version;
import pobj.pkgman.log.ILogger;
import pobj.pkgman.log.LogBuffer;
import pobj.pkgman.log.PkgLogger;

public class PkgLoggerTest {
	
	@Test public void test() {
		ILogger log = new LogBuffer();
		IPkg pkg = new LimitPkg("paquet", new Version(2,0), Collections.emptyList());
		IPkg deco = new PkgLogger(pkg, log);
		deco.install();
		assertEquals("Installing paquet-2.0\nSuccess\n", log.getLog());
		deco.uninstall();
		assertEquals("Installing paquet-2.0\nSuccess\nUninstalling paquet-2.0\n", log.getLog());
	}
	
}
