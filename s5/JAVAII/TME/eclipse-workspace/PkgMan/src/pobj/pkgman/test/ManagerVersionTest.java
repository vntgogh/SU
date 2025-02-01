package pobj.pkgman.test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.IOException;
import java.util.List;

import org.junit.Test;

import pobj.pkgman.IPkg;
import pobj.pkgman.ManagerVersion;
import pobj.pkgman.loader.PkgLoader;

public class ManagerVersionTest {

	@Test public void testInstall() throws IOException {
		// Chargement du fichier example.txt
		PkgLoader loader = new PkgLoader("src/pobj/pkgman/loader/example.txt"); 
		List<IPkg> pkgs = loader.getPackages();

		// Installation de Java 7
		ManagerVersion m = new ManagerVersion();
		assertTrue(m.installPkg(pkgs.get(0)));
		assertTrue(m.getInstalled().contains(pkgs.get(0)));

		// Installation de JUnit 4.0, qui met à jour Java 
		assertTrue(m.installPkg(pkgs.get(2)));
		assertFalse(m.getInstalled().contains(pkgs.get(0)));
		assertTrue(m.getInstalled().contains(pkgs.get(1)));
		assertTrue(m.getInstalled().contains(pkgs.get(2)));
	
		// Installation d'Eclipse, qui ne met rien à jour
		assertTrue(m.installPkg(pkgs.get(3)));
		assertFalse(m.getInstalled().contains(pkgs.get(0)));
		assertTrue(m.getInstalled().contains(pkgs.get(1)));
		assertTrue(m.getInstalled().contains(pkgs.get(2)));
		assertTrue(m.getInstalled().contains(pkgs.get(3)));
	}

}
