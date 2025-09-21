package pobj.pkgman.test;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.Test;

import pobj.pkgman.IManager;
import pobj.pkgman.ManagerVersion;
import pobj.pkgman.updater.Connector;
import pobj.pkgman.updater.IConnector;
import pobj.pkgman.updater.UpdateException;
import pobj.pkgman.updater.Updater;

public class UpdaterTest {

	@Test public void test1() throws UpdateException {
		IConnector c = new Connector("src/pobj/pkgman/loader/example.txt");
		IManager m = new ManagerVersion();
		Updater  u = new Updater(c, m);
		assertTrue(u.getInstalled().isEmpty());

		ArrayList<String> s = new ArrayList<>();
		s.add("eclipse");
		u.installPkgs(s);
		assertTrue(u.getInstalled().contains("eclipse"));
		assertTrue(u.getInstalled().contains("java"));
	}

	@Test(expected=UpdateException.class)
	public void test2() throws UpdateException {
		IConnector c = new Connector("src/pobj/pkgman/loader/example.txt");
		IManager m = new ManagerVersion();
		Updater  u = new Updater(c, m);
		assertTrue(u.getInstalled().isEmpty());

		ArrayList<String> s = new ArrayList<>();
		s.add("unknown");
		u.installPkgs(s);
	}
}
