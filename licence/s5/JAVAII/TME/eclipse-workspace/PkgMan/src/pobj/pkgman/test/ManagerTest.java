package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.IOException;
import java.util.List;

import org.junit.Test;

import pobj.pkgman.IPkg;
import pobj.pkgman.Manager;
import pobj.pkgman.loader.PkgLoader;

public class ManagerTest {

	@Test public void testInstall() throws IOException {
		// Chargement du fichier example.txt
		PkgLoader loader = new PkgLoader("src/pobj/pkgman/loader/example.txt"); 
		List<IPkg> pkgs = loader.getPackages();

		// Installation d'Eclipse 4.6, qui doit installer tous les paquets
		Manager m = new Manager();
		assertTrue(m.installPkg(pkgs.get(3)));
		
		// Vérification que tous les paquets sont installés
		assertTrue(m.getInstalled().contains(pkgs.get(0)));
		assertTrue(m.getInstalled().contains(pkgs.get(1)));
		assertTrue(m.getInstalled().contains(pkgs.get(2)));
		assertTrue(m.getInstalled().contains(pkgs.get(3)));
		assertEquals(4, m.getInstalled().size());
		
		// Désinstallation d'Eclipse 4.6
		m.uninstallPkg(pkgs.get(3));
		
		// Vérification des paquets encore installés
		assertTrue(m.getInstalled().contains(pkgs.get(0)));
		assertTrue(m.getInstalled().contains(pkgs.get(1)));
		assertTrue(m.getInstalled().contains(pkgs.get(2)));
		assertFalse(m.getInstalled().contains(pkgs.get(3)));
		assertEquals(3, m.getInstalled().size());
	}

}
